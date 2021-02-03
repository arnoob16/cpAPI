import requests
import json
from datetime import datetime
from pytz import timezone


def getHackerearthContests():
    response = requests.get(
        "https://www.hackerearth.com/chrome-extension/events/")
    hackerearthContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["response"]
        for contest in contests:
            hackerearthContest = {}
            hackerearthContest["platform"] = "HackerEarth"
            if contest["status"] == "UPCOMING":
                hackerearthContest["contestName"] = contest["title"]
                hackerearthContest["contestLink"] = contest["url"]
                start = contest["start_tz"][0: contest["start_tz"].rindex(
                    ':')] + contest["start_tz"][contest["start_tz"].rindex(':')+1:]
                start = start.replace(" ", "T")
                end = contest["end_tz"].replace(" ", "T")
                try:
                    hackerearthContest["startTime"] = datetime.strptime(
                        start, '%Y-%m-%dT%H:%M:%S%z').astimezone(timezone('Asia/Kolkata')).strftime('%Y-%m-%dT%H:%M:%S%z')
                    td = datetime.strptime(
                        end, '%Y-%m-%dT%H:%M:%S%z') - datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
                    if td.days and td.seconds:
                        hackerearthContest["contestDuration"] = str(
                            td.days) + " Days & " + str((td.seconds)//3600) + " hours."
                    elif td.days:
                        hackerearthContest["contestDuration"] = str(
                            td.days) + " Days"
                    elif td.seconds and td.seconds > 3600:
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
                        hackerearthContest["contestDuration"] = hours + \
                            ":" + mins + " hours."
                    if hackerearthContest["contestDuration"]:
                        hackerearthContests.append(hackerearthContest)
                except:
                    continue
    return hackerearthContests
