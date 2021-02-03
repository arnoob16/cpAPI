from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime


def getCodechefContests():
    response = requests.get("https://www.codechef.com/contests/")
    codechefContests = []
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        contests = soup.select(".content-wrapper > div")[3].find_all("tr")
        contests.pop(0)
        for contest in contests:
            elements = contest.select("td")
            elements.pop(0)
            codechefContest = {}
            codechefContest["platform"] = "CodeChef"
            codechefContest["contestName"] = elements[0].text.strip()
            codechefContest["contestLink"] = "https://www.codechef.com"+elements[0].select("a")[0].get("href")
            codechefContest["startTime"] = elements[1].get(
                "data-starttime").replace('+05:30', '+0530')
            start = datetime.strptime(
                codechefContest["startTime"][0: codechefContest["startTime"].index('+')], '%Y-%m-%dT%H:%M:%S')
            end = datetime.strptime(elements[2].get(
                "data-endtime")[0:elements[2].get("data-endtime").index("+")], '%Y-%m-%dT%H:%M:%S')
            td = (end - start)
            print(td)
            totalSeconds = td.total_seconds()
            days = int(totalSeconds//86400)
            remainingSeconds = totalSeconds%86400
            hours = int(remainingSeconds//3600)
            remainingSeconds = remainingSeconds%3600
            minutes = int(remainingSeconds//60)

            contestDuration = ""
            if days:
                contestDuration += str(days)+" Days, "
            if hours:
                contestDuration += str(hours)+" Hours, "
            if minutes:
                contestDuration += str(minutes)+" Minutes"
            codechefContest["contestDuration"] = contestDuration

            codechefContests.append(codechefContest)
    return codechefContests
