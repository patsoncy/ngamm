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

# TODO: 1、多线程 2、图片名字对应楼层 3、模块化

def main():
    try:
        urls = utils.get_urls_from_properties(setting.properties_name)
    except IOError:
        print '配置文件不存在或没有待请求的地址'
    else:
        let_us_go(urls)


def let_us_go(urls):
    for url in urls:
        try:
            # 获得帖子源码
            post_content = get_url_content(url)
            print post_content
            if not post_content:
                raise IOError('%s 内容获取失败，检查请求状态' % url)
                break
            # 获得帖子标题
            post_image_dir_name = dry_nga_title(get_post_title(post_content))
            print 'post title : %s' % post_image_dir_name
            if post_image_dir_name == '提示信息':
                print 'cookie已过期 请检查'
                break
            # 获得帖子页数
            post_pages = get_post_total_pages(post_content)
            print 'post pages : %s' % post_pages
            # 生成帖子图片文件夹
            img_path = make_post_image_dir(post_image_dir_name)
            print 'post image dir : %s' % img_path
            # 获得帖子所有图片http路径
            img_links = fetch_post_image_links(url, post_pages)
            # 删除已经下载过的图片链接
            new_img_links = remove_repeat_img_links(img_path, post_image_dir_name, img_links)
            print 'Total download link: %s' % len(new_img_links)
            # 下载图片
            download_images_from_link_list(new_img_links, img_path)
        except IOError, e:
            print e


def get_url_content(url):
    response = requests.get(url, headers=nga_headers_cookies.headers, cookies=nga_headers_cookies.cookies())
    if response.status_code != 200:
        print 'Request (%s)\'s false,status_code = %s' % (url, response.status_code)
        print response.content
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
    post_content_reg = re.compile(setting.post_content_pattern, re.S)
    link_reg = re.compile(setting.img_link_pattern)
    link_reg2 = re.compile(setting.img_link_with_third_site_pattern)
    img_links = []
    for page in range(1, post_pages + 1):
        print 'cur page:%s' % page
        curl_page_url = utils.make_url_with_page_num(url, page)
        content = (re.findall(post_content_reg, get_url_content(curl_page_url)))[0]
        origin_img_links = re.findall(link_reg, content) + re.findall(link_reg2, content)
        img_links += [utils.make_real_img_link(link) for link in origin_img_links]
    return sorted(utils.clean_str_list(img_links))


def remove_repeat_img_links(img_path, post_image_dir_name, img_links):
    record_file_path = img_path + post_image_dir_name + '.txt'
    print 'Post download record file: %s' % record_file_path
    if os.path.exists(record_file_path):
        download_records_file = open(record_file_path, 'r+')
        # 下载过的图片链接
        existed_links = utils.clean_str_list(download_records_file.readlines())
        # 新增链接（所有链接减去已下载链接）
        new_links = sorted(list(set(img_links) - set(existed_links)))
        # 将新增连接追加写入至记录文件
        download_records_file.writelines([link + '\n' for link in new_links])
        download_records_file.close()
        return new_links
    else:
        download_records_file = open(record_file_path, 'w')
        download_records_file.writelines([link + '\n' for link in img_links])
        download_records_file.close()
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


def download_images_from_link_list(img_links, img_path):
    for index, link in enumerate(img_links):
        urllib.urlretrieve(link, filename=img_path + '\\' + utils.clean_filename(link[link.rfind('/') + 1:]))


if __name__ == '__main__':
    main()
