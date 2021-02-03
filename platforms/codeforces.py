import requests
import json
from datetime import datetime


def getCodeforcesContests():
    response = requests.get("https://codeforces.com/api/contest.list")
    codeforcesContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["result"]
        for contest in contests:
            if contest["phase"] == "BEFORE":
                codeforcesContest = {}
                codeforcesContest["platform"] = "CodeForces"
                codeforcesContest["contestName"] = contest["name"]
                codeforcesContest["contestLink"] = "https://codeforces.com/contests/" + str(contest["id"])
                codeforcesContest["startTime"] = datetime.strftime(datetime.fromtimestamp(
                    contest["startTimeSeconds"]), '%Y-%m-%dT%H:%M:%S') + '+0530'
                codeforcesContest["contestDuration"] = "0" + \
                    str(contest["durationSeconds"]//3600) + ":00 hours."
                codeforcesContests.append(codeforcesContest)
    return codeforcesContests
