# -*- coding:utf-8 -*-


# 下载网页
import urllib
import urllib2
import urlparse
from Config import *


def download(url, user_agent='wswp',values=None, proxy=True, num_retries=2):
    """
    :param url:下载地址
    :param user_agent:用户代理
    :param values:参数，用于post和get
    :param proxy:代理是否开启，默认开启
    :param num_retries: 重新下载次数,默认2次
    :return:
    """
    print "download:", url
    headers = {'User-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    if values is not None:
        data = urllib.urlencode(values)
        request = urllib2.Request(url,data, headers=headers)
    else:
        request = urllib2.Request(url,headers=headers)
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler,httpsHandler)
    # opener = setProxy(opener,proxy)
    print "3",proxy
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request,timeout=TIMEOUT).read()
        # html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'URLError:', e.reason
        html = None
        if (num_retries > 0):  # 重新下载
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, proxy, num_retries - 1)
    return html


def setProxy(opener,proxy):
    enable_proxy = proxy
    proxy_header = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener.add_handler(proxy_header)
    else:
        opener.add_handler(null_proxy_handler)
    return opener

"""
header 属性:
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
"""