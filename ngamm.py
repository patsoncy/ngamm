#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'

import time
import re
import requests
import sys,os

url_prefix = 'http://bbs.nga.cn/read.php?tid=8369832&_ff=-7&rand=498&page='
img_prefix = 'http://img.nga.cn/attachments'

total_pages = 41

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'RA-Sid': '6FC61A40-20150702-064121-0537c4-21ecf4',
    'RA-Ver': '3.0.2',
    'Host': 'bbs.nga.cn',
    'If-Modified-Since':'Tue, 14 Jul 2015 15:21:24 GMT',
    'If-None-Match':'guest',
    'Referer':'http://bbs.nga.cn/read.php?tid=8369832&_ff=-7&rand=44'
}

now = str(int(round(time.time())))
print now
cookies = {
    'CNZZDATA30039253': 'cnzz_eid%3D443157492-1436882676-%26ntime%3D1436882676',
    'CNZZDATA30043604': 'cnzz_eid%3D710699211-1436884139-%26ntime%3D1436884139',
    'guestJs': '1436889127',
    'lastvisit': '1436889127',
    'ngaPassportUid': 'guest055a52d5013d0a'
}
img_list = []
for i in range(1,total_pages):
    url = url_prefix + str(i)
    web = requests.request('get', url, headers=headers, cookies=cookies)
    content = web.content
    # content_file = open('content.html','w')
    # content_file.write(content)
    # content_file.close()

    title_re = re.compile(r'<title>(.*?)</title>')
    img_re = re.compile(r'\[img\](\..*?)\[/img\]')

    dir_name = re.findall(title_re, content)
    all_img_list = re.findall(img_re, content)

    img_list = img_list + [img_prefix + s[1:] if (s.find('.thumb') == -1) else img_prefix + s[1:s.find('.thumb')] for s in
                all_img_list]

    file_path = sys.path[0] + '\\' + dir_name[0]

    if not os.path.exists(file_path):
        os.mkdir(file_path)

for img_link in set(img_list):
    name = img_link[-15:-5]
    img = open(file_path + '\\%s.jpg' % name, 'wb')
    img_stream = requests.get(img_link)
    img.write(img_stream.content)
    img.close()
