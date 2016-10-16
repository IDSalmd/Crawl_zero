#coding=utf-8

import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue

def download(url, headers, proxy, num_retries, data=None):
    print 'Downloading:',url
    #构造一个请求信息，返回的req就是一个构造好的请求
    requset = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyBasicAuthHandler(proxy_params))
    try:
        response = opener.open(requset)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Downoad error:',e.reason
        html = ''
        if hasattr(e,'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # 5XX错误
                return download(url, headers, proxy, num_retries-1, data)
        else:
            code = None
    return html

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1,
                 headers=None, user_agent='wswp', proxy=None,num_retries=1):
    '''
    在seed url里面按照link_regex抓取
    :param seed_url:
    :param link_regex:
    :param delay:
    :param max_depth:
    :param max_urls:
    :param headers:
    :param user_agent:
    :param proxy:
    :param num_retries:
    :return:
    '''
    #待抓取的url队列
    crawl_queue = Queue.deque([seed_url])
    #已经抓取的url和深度
    seen = {seed_url:0}
    #url计数，有多少个url已经被下载了
    num_urls = 0
    rp = get_robots(seed_url)
    #throttle = Throttle(delay)


def get_robots(url):
    '''
    获取网站rebotsw文件
    :param url:
    :return:
    '''
    # robotparser  tobots解析模块
    rp = robotparser.RobotFileParser()
    url = urlparse.urljoin(url, '/robots.txt')
    print url
    rp.set_url(url)
    rp.read()
    return rp
