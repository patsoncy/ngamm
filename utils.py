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
        if urls:
            



def make_url_with_page_num(url, page_no=1):
    return url + setting.url_suffix + str(page_no)


def make_real_img_link(img_link):
    return setting.img_link_prefix + img_link
