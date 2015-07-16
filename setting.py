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

# 帖子正文内容(python正则通配符 . 不包含换行符！！要匹配换行符在re.complie方法第三个参数加上re.S。
# re.S代表多行匹配！！！坑死我了！！！)
post_content_pattern = r'<div id=\'m_nav\' class=\'module_wrap\'>(.*?)<div class=\'module_wrap\'>'

# 获取图片相对地址的正则
img_link_pattern = r',url:\'(.*?)\',name:'

# 获取第三方图片地址的正则
img_link_with_third_site_pattern = r'\[img\](.*?)\[/img\]'

# 获取图片地址和名称的正则
img_link_and_name_pattern = r',url:\'(.*?)\',name:\'(.*?)\''

# 获取帖子名称的正则，用作文件夹名字
post_title_pattern = r'<title>(.*?)</title>'

# 获取帖子总页数正则
post_page_num_pattern = r',1:([0-9]*?),'
