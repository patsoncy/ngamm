#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patson'
import time

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
    # 'If-Modified-Since': 'Tue, 14 Jul 2015 15:21:24 GMT',
    # 'If-None-Match': 'guest',
    'Referer': 'http://bbs.nga.cn/read.php?tid=8369832&_ff=-7&rand=44'
}


def cookies():
    now = str(int(round(time.time())))
    return {
        'CNZZDATA30039253': 'cnzz_eid%3D443157492-1436882676-%26ntime%3D1436882676',
        'CNZZDATA30043604': 'cnzz_eid%3D710699211-1436884139-%26ntime%3D1436884139',
        'guestJs': now,
        'lastvisit': now,
        'ngaPassportUid': 'guest055a7ba0238964'
    }
