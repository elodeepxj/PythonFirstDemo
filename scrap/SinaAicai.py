# -*- coding:utf-8 -*-

from Config import *
import BeautifulSoupUtils
import json


def get_data(cur, conn):
    match_season_min = 2003
    match_season_max = match_season_min + 1
    round = 4
    flag = True
    while (flag):
        if(match_season_min == 2017 and match_season_max == 2018 and round == 21):
            print "flag = false"
            flag = False
        else:
            if(round < 39):
                details = BeautifulSoupUtils.get_beautiful_soup(
                    AICAI_DETAILS_URL % ((str)(match_season_min) + "-" + (str)(match_season_max), (str)(round)))
                details = details.find_all("p")
                print details
                for detail in details:
                    json_result = json.loads(detail.getText())
                    print json_result
                    status = json_result['status']
                    if (status == "success"):
                        result = json_result['result']
                        match_list = result['matchList']
                        if match_list:
                            for match in match_list:
                                id = match['id']
                                league = match['leagueName']
                                host_team = match['hostTeamName']
                                visit_team = match['awayTeamName']
                                host_score = match['hostScore']
                                visit_score = match['awayScore']
                                host_half_score = match['hostHalfScore']
                                visit_half_score = match['awayHalfScore']
                                host_rank = match['hostRank']
                                visit_rank = match['awayRank']
                                win_odds = match['winOdds']
                                win_rate = match['winRate']
                                lose_odds = match['loseOdds']
                                lose_rate = match['loseRate']
                                draw_odds = match['drawOdds']
                                draw_rate = match['drawRate']
                                match_result = match['matchResult']
                                match_time = match['matchTimeStr']
                                asia_tape_result = match['asiaTapeResult']
                                print host_team, visit_team
                                cur.execute(
                                    "insert into " + TN_AICAI_FRANCE + " values( '% s', '% s', '% s', '% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s','% s')" % (
                                        id, league, host_team, visit_team, host_score, visit_score, host_half_score,
                                        visit_half_score,
                                        host_rank, visit_rank, win_odds, win_rate, lose_odds, lose_rate, draw_odds, draw_rate,
                                        match_result, match_time, asia_tape_result,match_season_min))
                            conn.commit()
                            round += 1
            else:
                match_season_min+=1
                match_season_max+=1
                round = 1