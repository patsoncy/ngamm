# ngamm

> python练习，起因是看了一个晒老婆的nga帖子，就想写个脚本把图片都抓下来，送晒的人上雷霆崖，所以项目名称就叫ngamm

## 用途： 抓取nga论坛帖子图片的爬虫脚本

1. 帖子地址写在 `post_urls.txt` 里面，一行一个，`#`号开头的会被忽略
2. `python ngamm.py`
3. 下载的图片保存在pictures文件夹中，文件夹名为帖子名称

### version 0.1.1

专业python爬虫库有 `scrapy`

还有个叫`beautiful_soup` 的，类似于java的jsoup，解析dom树的

## TODO:
* 多个帖子用多进程，帖子中的多个url用多线程.multiprocess
* 增加日志装饰器

