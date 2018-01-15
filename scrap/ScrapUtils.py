# -*- coding:utf-8 -*-

import DBUtils
import ChineseCaiPiao
import SinaAicai

conn = DBUtils.connect_mysql()
cur = conn.cursor()


SinaAicai.get_data(cur=cur,conn=conn)

# chinese caipiao net
# ChineseCaiPiao.get_chinese_caipiao(cur=cur,conn=conn)


# DBUtils.create_table(cur=cur, table_name=TABLE_NAME)

# soup = BeautifulSoupUtils.get_beautiful_soup(BASE_URL)
# selects = soup.find_all('select')
# dates = []
# for select in selects:
#     datas = select.find_all('option')
#     for data in datas:
#         print data.getText()
#         dates.append(data.getText())
#
# print dates

# for date in dates:
#     details = BeautifulSoupUtils.get_beautiful_soup(DETAILS_URL + date)
#     details = details.find_all("p")
#     for detail in details:
#         # print detail.getText()
#         addedSingleQuoteJsonStr = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", detail.getText())
#         doubleQuotedJsonStr = addedSingleQuoteJsonStr.replace("'", "\"")
#         # print doubleQuotedJsonStr
#         json_result = json.loads(doubleQuotedJsonStr)
#         # print json_result.keys()
#         json_data = json_result['data']
#         # print json_data
#         scores = json_data["bonusCode"].replace(',', '')
#         matchs = json_data['match']
#         for i in range(len(matchs)):
#             mid = matchs[i]['mid']
#             league = matchs[i]['league']
#             host = matchs[i]['host']
#             visit = matchs[i]['visit']
#             score = scores[i]
#             cur.execute(
#                 "insert into " + TABLE_NAME + " values( '% s', '% s', '% s', '% s','%s')" % (
#                 mid, league, host, visit, score))

cur.close()
conn.close()
