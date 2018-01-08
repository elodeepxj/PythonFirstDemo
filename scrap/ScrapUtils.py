# -*- coding:utf-8 -*-

import BeautifulSoupUtils
from Config import *
import json
import re

soup = BeautifulSoupUtils.get_beautiful_soup(BASE_URL)
selects = soup.find_all('select')
dates = []
for select in selects:
    datas = select.find_all('option')
    for data in datas:
        print data.getText()
        dates.append(data.getText())

print dates
for date in dates:
    details = BeautifulSoupUtils.get_beautiful_soup(DETAILS_URL+date)
    details = details.find_all("p")
    for detail in details:
        print detail.getText()
        addedSingleQuoteJsonStr = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", detail.getText())
        doubleQuotedJsonStr = addedSingleQuoteJsonStr.replace("'", "\"")
        print doubleQuotedJsonStr
        json_result = json.loads(doubleQuotedJsonStr)

