#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'

import re
import requests
import os
import urllib
import nga_headers_cookies
import setting
import utils
import time
from utils import print_log


# TODO: 1、多进程 2、日志装饰器

def main():
    try:
        urls = utils.get_urls_from_txt_file(setting.urls_file_name)
    except IOError:
        print '配置文件不存在或没有待请求的地址'
    else:
        for url in urls:
            try:
                let_us_go(url)
            except IOError, e:
                print e
                break


def let_us_go(url):
    try:
        print '\n\n'
        # 获得帖子源码
        post_content = get_url_content(url)
        if not post_content:
            raise IOError('%s 内容获取失败，检查请求状态' % url)
        # 获得帖子标题
        post_image_dir_name = dry_nga_title(get_post_title(post_content))
        print '标题 : %s' % post_image_dir_name
        # 获得帖子页数
        post_pages = get_post_total_pages(post_content)
        print '页数 : %s' % post_pages
        # 生成帖子图片文件夹
        img_path = make_post_image_dir(post_image_dir_name)
        print '图片存放目录名 : %s' % img_path
        # 存放已下载链接的txt文件名
        record_file_name = img_path + post_image_dir_name + '.txt'
        # 获得帖子所有图片http路径
        img_links = fetch_post_image_links(url, post_pages)
        # 删除已经下载过的图片链接
        print_log('开始删除重复链接')
        new_img_links = remove_repeat_img_links(record_file_name, img_links)
        print_log('删除重复链接完毕')
        print '下载图片数: %s' % len(new_img_links)
        # 下载图片
        download_images_from_link_list(new_img_links, img_path, record_file_name)
    except IOError, e:
        print e


def get_url_content(url):
    response = requests.get(url, headers=nga_headers_cookies.headers, cookies=nga_headers_cookies.cookies())
    if response.status_code != 200:
        print 'Request (%s)\'s false,status_code = %s' % (url, response.status_code)
        return ''
    else:
        return response.content


def get_post_title(content):
    reg = re.compile(setting.post_title_pattern)
    title = re.findall(reg, content)
    return title[0] if title else 'default'


def dry_nga_title(nga_post_title):
    return nga_post_title if nga_post_title.find('艾泽拉斯国家地理论坛') == -1 \
        else nga_post_title[:nga_post_title.rfind('艾泽拉斯国家地理论坛') - 3]


def get_post_total_pages(content):
    reg = re.compile(setting.post_page_num_pattern)
    pages_num = re.findall(reg, content)
    return int(pages_num[0]) if pages_num else 1


def fetch_post_image_links(url, post_pages):
    print_log('开始收集帖子全部图片链接')
    post_content_reg = re.compile(setting.post_content_pattern, re.S)
    link_reg = re.compile(setting.img_link_pattern)
    link_reg2 = re.compile(setting.img_link_with_third_site_pattern)
    img_links = []
    for page in range(1, post_pages + 1):
        print '当前页数:%s\r' % page,
        curl_page_url = utils.make_url_with_page_num(url, page)
        whole_content = get_url_content(curl_page_url)
        if whole_content:
            content = (re.findall(post_content_reg, whole_content))[0]
            origin_img_links = re.findall(link_reg, content) + re.findall(link_reg2, content)
            img_links += [utils.make_real_img_link(link) for link in origin_img_links]
    print_log('收集链接完毕')
    return sorted(utils.clean_str_list(img_links))


def remove_repeat_img_links(record_file_name, img_links):
    if os.path.exists(record_file_name):
        download_records_file = open(record_file_name, 'r+')
        # 下载过的图片链接
        existed_links = utils.clean_str_list(download_records_file.readlines())
        # 新增链接（所有链接减去已下载链接）
        new_links = sorted(list(set(img_links) - set(existed_links)))
        # 将新增连接追加写入至记录文件 （废弃，改为下好一张存一张的地址）
        # download_records_file.writelines([link + '\n' for link in new_links])
        download_records_file.close()
        return new_links
    else:
        # download_records_file = open(record_file_path, 'w')
        # download_records_file.writelines([link + '\n' for link in img_links])
        # download_records_file.close()
        return img_links


def make_post_image_dir(post_image_dir_name):
    """生成存放帖子图片的文件夹.
    :param post_image_dir_name:文件夹名称
    :return 文件夹完整路径
    """
    # 生成 pictures 文件夹
    parent_dir = setting.project_path + setting.post_images_pardir
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)
    # 生成帖子文件夹
    real_dir = parent_dir + post_image_dir_name
    if not os.path.exists(real_dir):
        os.mkdir(real_dir)
    return real_dir + '\\'


def download_images_from_link_list(img_links, img_path, record_file_name):
    print_log('遍历下载图片中')
    start_time = time.time()
    total = len(img_links)
    record_file = open(record_file_name,'a')
    for index, link in enumerate(img_links):
        print_log('第 %s / %s 张' % (str(index + 1), total))
        urllib.urlretrieve(link, filename=img_path + '\\' + utils.clean_filename(link[link.rfind('/') + 1:]),
                           reporthook=schedule)
        record_file.write(link + '\n')
    end_time = time.time()
    record_file.close()
    print_log('遍历下载图片共花费 : %s 秒 ' % str(round(end_time - start_time, 2)))


def schedule(a, b, c):
    """下载进度
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%\r' % per,


if __name__ == '__main__':
    main()
