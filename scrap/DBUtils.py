# -*- coding:utf-8 -*-

import pymysql
import MySQLdb
from Config import *
import re


def connect_mysql():
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB_NAME, use_unicode=True,
                           charset=CHARSET,)
    return conn;


def create_table(cur, table_name):

    cur.execute(
        "create table if not exists " + table_name + "(league varchar(20),host varchar(30),visit varchar(30),win_lose varchar(10))")


def exist_of_table(cur,table_name):
    sql_show_tables = "SHOW_TABLES;"
    cur.execute(sql_show_tables)
    tables=[cur.fetchall()]

    table_list = re.findall()
