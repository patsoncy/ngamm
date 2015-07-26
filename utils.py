#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patson'

import setting
import os
import re


def get_urls_from_txt_file(file_name):
    if not os.path.exists(file_name):
        raise IOError
    else:
        properties = open(file_name, 'r')
        urls = properties.readlines()
        properties.close()
        if not urls:
            raise IOError
        else:
            # 排除被注释的url
            del_discard_url = [url for url in urls if not url.lstrip().startswith('#')]
            return clean_str_list(del_discard_url)


# 字符串型list去重去空
def clean_str_list(str_list):
    clean_list = [i.strip() for i in str_list if isinstance(i, str) and i.strip()]
    return list(set(clean_list))


def make_url_with_page_num(url, page_no=1):
    return url + setting.url_suffix + str(page_no)


def make_real_img_link(img_link):
    if img_link.find('http') == -1:
        link_prefix = setting.img_link_prefix + '/'
        img_link = img_link[2:] if img_link.startswith('./') else img_link
        if img_link.find('.thumb') != -1:
            index = img_link.find('.thumb')
        elif img_link.find('.medium') != -1:
            index = img_link.find('.medium')
        else:
            index = None
        real_link = link_prefix + img_link[:index]
        return real_link
    else:
        return img_link


# 去除Windows系统下文件夹名称的特殊字符,使用 - 代替
def clean_filename(file_name):
    return re.sub(r'>|<|:|/|\||\\|\?|\*|"', r'-', file_name)


def print_log(words):
    print '-' * 20, words, '-' * 20
