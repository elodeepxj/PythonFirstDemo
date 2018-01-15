# -*- coding:utf-8 -*-
from Config import *
import BeautifulSoupUtils
import json
import re


def get_chinese_caipiao(cur,conn):
    year = 2016
    stage = 177
    flag = True;
    while flag:
        str_stage = ((str)(stage)).zfill(3)
        print str_stage
        details = BeautifulSoupUtils.get_beautiful_soup(DETAILS_URL + (str)(year)+str_stage)

        print details
        details = details.find_all("p")
        for detail in details:
            # print detail.getText()
            addedSingleQuoteJsonStr = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", detail.getText())
            doubleQuotedJsonStr = addedSingleQuoteJsonStr.replace("'", "\"")
            print doubleQuotedJsonStr
            json_result = json.loads(doubleQuotedJsonStr)
            # print json_result.keys()
            ret = json_result['ret']
            if (ret is False):
                year+=1
                stage = 0
                if(year == 2018 and stage > 1):
                    flag = False
            else:
                json_data = json_result['data']
                scores = json_data["bonusCode"].replace(',', '')
                matchs = json_data['match']
                for i in range(len(matchs)):
                    mid = matchs[i]['mid']
                    league = matchs[i]['league']
                    host = matchs[i]['host']
                    visit = matchs[i]['visit']
                    score = scores[i]
                    print mid,league,host,visit,score
                    cur.execute(
                        "insert into " + TN_CHINA_CAIPIAO + " values( '% s', '% s', '% s', '% s','%s')" % (mid, league, host, visit, score))
        conn.commit()
        print "insert success"
        stage+=1