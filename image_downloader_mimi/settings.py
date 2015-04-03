# -*- coding: utf-8 -*-

# Scrapy settings for image_downloader_mimi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'image_downloader_mimi'

SPIDER_MODULES = ['image_downloader_mimi.spiders']
NEWSPIDER_MODULE = 'image_downloader_mimi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'image_downloader_mimi (+http://www.yourdomain.com)'

IMAGE_MIN_HEIGHT = 500
IMAGE_MIN_WIDTH = 500
DOWNLOAD_TIMEOUT = 120
IMAGES_STORE = 'download'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}