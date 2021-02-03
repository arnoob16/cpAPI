from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from pytz import timezone


def getAtCoderContests():
    response = requests.get("https://atcoder.jp/contests/")
    atCoderContests = []
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        contests = soup.select("#contest-table-upcoming tbody tr")
        for contest in contests:
            elements = contest.find_all("td")
            atCoderContest = {}
            atCoderContest["platform"] = "AtCoder"
            atCoderContest["contestName"] = elements[1].text.strip()[elements[1].text.strip().index(
                "\n")+1:]
            atCoderContest["contestLink"] = "https://atcoder.jp" + elements[1].select("a")[0].get("href")
            atCoderContest["startTime"] = datetime.strptime(elements[0].text.replace(
                " ", "T"), '%Y-%m-%dT%H:%M:%S%z').astimezone(timezone('Asia/Kolkata')).strftime('%Y-%m-%dT%H:%M:%S%z')
            atCoderContest["contestDuration"] = elements[2].text + " hours."
            atCoderContests.append(atCoderContest)
    return atCoderContests
