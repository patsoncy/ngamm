#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'
import re, urllib, setting
import unittest
import utils, os, ngamm

s = 'http://bbs.nga.cn/read.php?tid=8369832&_ff=-7&rand=498'

c = ngamm.get_url_content(s)
t = re.findall(re.compile(setting.post_content_pattern,re.S), c)
print t

# urllib.urlretrieve('http://img.nga.cn/attachments/mon_201507/14/-7_55a51d9e8dcd6.jpg','1.jpg')

# class MyTest(unittest.TestCase):
#     pass
