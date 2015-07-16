#!/usr/bin/env python
# -*- coding: gbk -*-

__author__ = 'patson'
import sys

# 工程路径
project_path = sys.path[0] + '\\'

# 配置文件名称
properties_name = 'post_urls.properties'

# 帖子图片存储父路径
post_images_pardir = 'pictures\\'

# 在帖子URL中添加页码
url_suffix = '&page='

# 图片域名地址
img_link_prefix = 'http://img.nga.cn/attachments'

# 获取图片相对地址的正则
img_link_pattern = r',url:\'(.*?)\',name:'

# 获取图片地址和名称的正则
img_link_and_name_pattern = r',url:\'(.*?)\',name:\'(.*?)\''

# 获取帖子名称的正则，用作文件夹名字
post_title_pattern = r'<title>(.*?)</title>'

# 获取帖子总页数正则
post_page_num_pattern = r',1:([0-9]*?),'

