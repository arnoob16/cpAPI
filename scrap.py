from platforms import atcoder, codechef, codeforces, hackerearth


def fetchContests():
    result = {}
    contests = []
    contests.extend(atcoder.getAtCoderContests())
    contests.extend(codechef.getCodechefContests())
    contests.extend(codeforces.getCodeforcesContests())
    contests.extend(hackerearth.getHackerearthContests())
    contests = sorted(contests, key=lambda contest: contest['startTime'])
    result["contests"] = contests
    return result
