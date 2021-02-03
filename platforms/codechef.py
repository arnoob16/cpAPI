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
            if td.seconds//3600 == 0:
                codechefContest["contestDuration"] = str(td.days) + " Days"
            else:
                hours = ""
                mins = ""
                if (td.seconds)//3600 < 10:
                    hours = "0" + str((td.seconds)//3600)
                else:
                    hours = (td.seconds)//3600
                if ((td.seconds)//60) % 60 < 10:
                    mins = "0" + str(((td.seconds)//60) % 60)
                else:
                    mins = ((td.seconds)//60) % 60
                codechefContest["contestDuration"] = str(
                    hours) + ":" + str(mins) + " hours."
            codechefContests.append(codechefContest)
    return codechefContests
