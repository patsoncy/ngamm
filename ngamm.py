#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'

import time
import re
import requests
import sys,os

url = 'http://bbs.nga.cn/read.php?tid=8369832&_ff=-7'
img_prefix = 'http://img.nga.cn/attachments'

total_pages = 1

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'RA-Sid': '6FC61A40-20150702-064121-0537c4-21ecf4',
    'RA-Ver': '3.0.2'
}
cookies = {
    'CNZZDATA30039253': 'cnzz_eid%3D2071077818-1436855676-%26ntime%3D1436855676',
    'CNZZDATA30043604': 'cnzz_eid%3D928829673-1436856282-%26ntime%3D1436856282',
    'guestJs': str(int(round(time.time()))),
    'lastvisit': str(int(round(time.time()))),
    'ngaPassportUid': 'guest055a4bcff6d2dc'
}

web = requests.request('get', url, headers=headers, cookies=cookies)
content = web.content

title_re = re.compile(r'<title>(.*?)</title>')
img_re = re.compile(r'\[img\](\..*?)\[/img\]')

dir_name = re.findall(title_re, content)
all_img_list = re.findall(img_re, content)

img_list = [img_prefix + s[1:] if (s.find('.thumb') == -1) else img_prefix + s[1:s.find('.thumb')] for s in
            all_img_list]

file_path = sys.path[0] + '\\' + dir_name[0]

if not os.path.exists(file_path):
    os.mkdir(file_path)

for img_link in img_list:
    print file_path + '\\%s.jpg' % img_link[-15:-5]
    img = open(file_path + '\\%s.jpg' % img_link[-5:-20], 'wb')
    img_stream = requests.get(img_link)
    img.write(img_stream.content)
    img.close()
