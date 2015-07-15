#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'

import time
import re
import requests
import sys
import os
import nga_headers_cookies
import setting

# TODO: 1、多线程 2、图片名字对应楼层 3、模块化
# url_prefix = 'http://bbs.nga.cn/read.php?tid=8344065&page='

web = requests.get(url_prefix + '4', headers=nga_headers_cookies.headers, cookies=nga_headers_cookies.cookies())
pat = re.compile(setting.post_page_num)
name = re.findall(pat, web.content)
print web.content
print name


# img_list = []
# file_path = 'default'
# for i in range(1, total_pages + 1):
#     url = url_prefix + str(i)
#     print url
#     web = requests.request('get', url, headers=nga_headers_cookies.headers, cookies=nga_headers_cookies.cookies())
#     content = web.content
#     if i == 1:
#         content_file = open('content.html', 'w')
#         content_file.write(content)
#         content_file.close()
#         title_re = re.compile(r'<title>(.*?)</title>')
#         dir_name = re.findall(title_re, content)
#         file_path = sys.path[0] + '\\image\\' + dir_name[0]
#
#     # img_re = re.compile(r'\[img\](\..*?)\[/img\]')
#     img_re = re.compile(r',url:\'(.*?)\',name:')
#     all_img_list = re.findall(img_re, content)
#     # img_list = img_list + [img_prefix + s[1:] if (s.find('.thumb') == -1) else img_prefix + s[1:s.find('.thumb')] for s
#     #                        in
#     #                        all_img_list]
#     img_list = img_list + [img_prefix + '/' + s if (s.find('.thumb') == -1) else img_prefix + '/' + s[:s.find('.thumb')]
#                            for s
#                            in
#                            all_img_list]
#
# if not os.path.exists(file_path):
#     os.mkdir(file_path)
#
# print img_list
# for img_link in set(img_list):
#     name = img_link[-15:-5]
#     img = open(file_path + '\\%s.jpg' % name, 'wb')
#     img_stream = requests.get(img_link)
#     img.write(img_stream.content)
#     img.close()


