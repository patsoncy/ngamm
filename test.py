#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'Administrator'
import re, urllib, setting
import unittest
import utils, os

s = 'aaa*aa<aa?aa>aa"aa|aaaa/aa\\aa:aaaa'
# fi = open(s,'r')
print re.sub(r'>|<|:|/|\||\\|\?|\*|"', r'-', s)

# urllib.urlretrieve('http://img.nga.cn/attachments/mon_201507/14/-7_55a51d9e8dcd6.jpg','1.jpg')

# class MyTest(unittest.TestCase):
#     pass
