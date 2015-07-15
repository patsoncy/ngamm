#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patson'

import setting
import os


def get_urls_from_properties(properties_name):
    if not os.path.exists(properties_name):
        raise IOError
    else:
        properties = open(properties_name, 'r')
        urls = properties.readlines()
        properties.close()
        if not urls:
            raise IOError
        else:
            return clean_str_list(urls)

# 字符串型list去重去空
def clean_str_list(str_list):
    clean_list = [i.strip() for i in str_list if isinstance(i,str) and i.strip()]
    return list(set(clean_list))

def make_url_with_page_num(url, page_no=1):
    return url + setting.url_suffix + str(page_no)

def make_real_img_link(img_link):
    return setting.img_link_prefix + img_link
