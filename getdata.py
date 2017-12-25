# -*- coding:utf-8 -*-
import requests
from config import *
from bs4 import BeautifulSoup
import datetime,time
import pymysql
# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf8")


def getWebData(url):
    url = url
    hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    r = requests.get(url, headers=hdrs)
    soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), 'lxml')
    return soup


# 雷锋网数据
# https://www.leiphone.com/
def getDataFrom_leiphone(url,soup):
    # 获取网页标题
    soup_title = soup.find('div', {'class': 'lphArticle-detail'})
    title = soup_title.get('data-article_seo_title')
    title = title.encode("utf-8")

    # 获取文章作者
    soup_author = soup.find('div', {'class': 'lphArticle-detail'})
    author = soup_author.get('data-author_name')
    author = author.encode("utf-8")

    # 来源网址
    reference_url = url[0].encode("utf-8")

    # 导语
    soup_introduction = soup.find('meta', {'name': 'description'})
    introduction = soup_introduction.get('content')
    introduction = introduction.encode("utf-8")

    # 发布时间
    release_time = soup.find('div',{'class':'msg'})
    release_time = release_time.find('td',{'class':'time'})
    release_time = release_time.next_element
    release_time = release_time.strip()
    release_time = release_time+":00"

    # 正文
    timp_main_body = ""
    soup_main_body = soup.find('div', {'class': 'info'})
    main_body = soup_main_body.find('div', {'class': 'lph-article-comView'})
    for child in main_body.select('p'):
        child = str(child)
        timp_main_body = timp_main_body+child
    #statement_content = main_body.find('a',{'href':'http://dwz.cn/4ErMxZ'}).parent.clear
    #print statement_content
    #main_body = main_body.encode("utf-8")
    main_body = timp_main_body.replace('雷锋网原创文章，未经授权禁止转载。详情见','')
    main_body = main_body.replace('转载须知','')

    # 声明
    # 雷锋网文章没有 声明
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    create_time=update_time = dt
    insert_name = (
        "INSERT INTO " + TABLE_NAME + "(title,author,introduction,main_body,reference_url,release_time,create_time,update_time,thumb_url)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    insert_data = (title, author, introduction, main_body, reference_url, release_time,create_time,update_time,url[1])
    return insert_name, insert_data,


# 机器之心数据
# https://www.jiqizhixin.com/
def getDataFrom_jiqizhixin(url,soup):
    # 获取网页标题
    soup_title = soup.find('meta', {'name': 'twitter:title'})
    title = soup_title.get('content')
    title = title.encode("utf-8")

    # 获取文章作者
    soup_author = soup.find('span', {'class': 'article-detail__author__name'})
    author = soup_author.next_element
    author = author.encode("utf-8")

    # 来源网址
    reference_url = url[0].encode("utf-8")

    # 导语
    soup_introduction = soup.find('meta', {'name': 'description'})
    introduction = soup_introduction.get('content')
    introduction = introduction.encode("utf-8")

    # # 发布时间
    soup_release_time = soup.find('span', {'class': 'article-detail__publish-date'})
    release_time = soup_release_time.next_element
    release_time = release_time.encode("utf-8")
    release_time = release_time.replace('年','-').replace('月','-').replace('日 ',' ') + ':00'
    release_time = datetime.datetime.strptime(release_time, '%Y-%m-%d %H:%M:%S')


    # 正文
    main_body = soup.find('div', {'class': 'article-detail__content'})
    main_body = main_body.encode("utf-8")

    # 声明
    soup_article_stated = soup.find('div', {'class': 'article-detail__copyright-content'})
    article_stated = soup_article_stated.next_element
    article_stated = article_stated.encode("utf-8")

    #创建和更新时间
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    create_time = update_time = dt

    insert_name = (
        "INSERT INTO " + TABLE_NAME + "(title,author,reference_url,introduction,release_time,main_body,article_stated,create_time,update_time,thumb_url)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    insert_data = (title, author, reference_url, introduction, release_time, main_body, article_stated,create_time,update_time,url[1])
    return insert_name, insert_data,


# http://www.52ai.com/
def getDataFrom_52AI(url,soup):
    # 获取网页标题
    title = soup.find('title')
    title = title.next_element
    title = title.encode("utf-8")

    # 获取文章作者
    soup_author = soup.find('meta', {'name': 'author'})
    author = soup_author.get('content')
    author = author.encode("utf-8")
    # 来源网址
    reference_url = url[0].encode("utf-8")
    # 导语
    soup_introduction = soup.find('meta', {'name': 'description'})
    introduction = soup_introduction.get('content')
    introduction = introduction.encode("utf-8")
    # 发布时间
    soup_release_time = soup.find('i', {'class': 'iconfont icon-time'})
    release_time = soup_release_time.next_element
    release_time = release_time.encode("utf-8")
    # 正文
    soup_main_body = soup.find('div', {'class': 'post-content'})
    main_body = soup_main_body.encode("utf-8")
    ## 声明
    ## 52AI文章没有 声明

    # 创建和更新时间
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    create_time = update_time = dt

    insert_name = (
        "INSERT INTO " + TABLE_NAME + "(title,author,introduction,main_body,reference_url,release_time,create_time,update_time,thumb_url)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    insert_data = (title, author, introduction, main_body, reference_url, release_time,create_time,update_time,url[1])
    return insert_name, insert_data,


#根据URL选择函数
def Select_Model(url, soup):
    if "www.jiqizhixin.com" in url[0]:
        return getDataFrom_jiqizhixin(url,soup)
    if "www.leiphone.com" in url[0]:
        return getDataFrom_leiphone(url, soup)
    if "www.52ai.com" in url[0]:
        return getDataFrom_52AI(url, soup)
    else:
        return None

def getLeifengURL_list(url,cur):
    soup = getWebData(url)
    soup = soup.find('div', {'class': 'lph-pageList index-pageList'})
    soup = soup.findAll('div', {'class': 'img'})
    url_list = []
    for soup_url in soup:
        thumb_url = soup_url.find('img', {'class': 'lazy'})
        thumb_url = thumb_url.get('data-original')
        soup_url = soup_url.find('a', {'target': '_blank'}).get('href')
        # 查询如若有已经存在则不再添加了，如果不存在则添加
        if cur.execute("SELECT * FROM "+TABLE_NAME+" WHERE reference_url = %s",soup_url) == 0:
            url_list.append((soup_url,thumb_url))
    return url_list

def getJiQIZhiXInURL_list(url,cur):
    soup = getWebData(url)
    soup = soup.findAll('div',{'class': 'article-inline__cover-container'})
    url_list = []
    for soup_url in soup:
        soup_url = soup_url.find('a', {'class':'article-inline__cover hover-zoom'})
        # 去除左右两边多余的字符
        thumb_url = soup_url.get('style').lstrip('background-image: url\(').rstrip(')')
        soup_url = url+soup_url.get('href')
        # 查询如若有已经存在则不再添加了，如果不存在则添加
        if cur.execute("SELECT * FROM "+TABLE_NAME+" WHERE reference_url = %s",soup_url) == 0:
            url_list.append((soup_url, thumb_url))
    return url_list

#http://www.52ai.com/AInews/
def get52AIURL_list(url,cur):
    soup = getWebData(url)
    soup = soup.findAll('div',{'class': 'media-left media-middle'})
    url_list = []
    for soup_url in soup:
        thumb_url = soup_url.find('img').get('src')
        soup_url = soup_url.find('a').get('href')
        #查询如若有已经存在则不再添加了，如果不存在则添加
        if cur.execute("SELECT * FROM "+TABLE_NAME+" WHERE reference_url = %s",soup_url) == 0 :
            url_list.append((soup_url, thumb_url))
    return url_list

#获取数据到数据库
def getData(url,conn):
    cur = conn.cursor()
    if "www.jiqizhixin.com" in url:
        url_list = getJiQIZhiXInURL_list(url,cur)
    elif "www.leiphone.com" in url:
        url_list = getLeifengURL_list(url,cur)
    elif "www.52ai.com" in url:
        url_list = get52AIURL_list(url,cur)
    else:
        url_list = None
    for url in url_list:
        soup = getWebData(url[0])
        if not Select_Model(url, soup) is None:
            insert_name, insert_data = Select_Model(url, soup)
            cur.execute(insert_name, insert_data)
            conn.commit()
        else:
            print "this URL is not defined!"
    return

#目前只支持这三个网站的数据
#url = "http://www.52ai.com/AInews/"
#url = "https://www.jiqizhixin.com/"
#url = "https://www.leiphone.com/"

def reptileData():
    url_list = ['http://www.52ai.com/AInews/',
                'https://www.jiqizhixin.com/',
                'https://www.leiphone.com/']
    conn = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        passwd=PASSWD,
        db=DB_NAME,
        use_unicode=USE_UNICODE,
        charset=CHARSET)
    for url in url_list:
        getData(url, conn)
    conn.close()







#调用爬数据
reptileData()