<p align="center">
<img height="250px" src="https://raw.githubusercontent.com/arnoob16/cpAPI/master/cpApiLogo.png?token=ALWD5TPXQ22W66D2BUNBYBDAD4OOW">
<h1 align="center">Competitive Programming Contests API</h1>

<p align="center">
    An API built to give you updates about the upcoming contests on various Competitive Coding platforms.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Contribution-Welcome-blue?style=for-the-badge">
<img src="https://img.shields.io/github/stars/arnoob16/cpAPI?color=gold&style=for-the-badge">
</p>

<p align="center">
<img src="https://img.shields.io/github/issues/arnoob16/cpAPI?style=for-the-badge&color=red">
<img src="https://img.shields.io/github/forks/arnoob16/cpAPI?style=for-the-badge">
<img src="https://img.shields.io/github/issues-pr-closed/arnoob16/cpAPI?color=green&style=for-the-badge">
</p>




---

<h3 align="center">Coding Platforms Supported</h3>

<p align="center">
    <img height="100px" src = "https://img.atcoder.jp/assets/atcoder.png"/>
    <img height="100px" src = "https://www.ime.usp.br/~arcjr/image/codeforces.png"/>
    <img height="100px" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXBUWY12NOXtKD9UEvtqkKeWAPyJm8GTkgEw&usqp=CAU"/>
</p>

<h6 align="center">More platforms will soon be supported.</h6>

---

<h3 align="center">
    How to use this API?
</h3>

- Send a `GET` request to https://cp-api.arnoob16.vercel.app/ URL.
- Response received is an Array of Contest Objects
- Each contest object has 4 parameters, 
    - `platform` => The coding platform that is hosting the contest.
    - `contestName` => The name of the contest.
    - `contestLink` => URL of the contest.
    - `startTime` => The starting timestamp of the contest.
    - `contestDuration` => The duration of the contest.

```
{
  "contests": [
    {
      "platform": "CodeChef",
      "contestName": "CP in 7 days",
      "contestLink": "https://www.codechef.com/CP7D2021?itm_campaign=contest_listing",
      "startTime": "2021-02-03T16:30:00+0530",
      "contestDuration": "02:30 hours."
    },
    {
      "platform": "CodeChef",
      "contestName": "February Challenge 2021",
      "contestLink": "https://www.codechef.com/FEB21?itm_campaign=contest_listing",
      "startTime": "2021-02-05T15:00:00+0530",
      "contestDuration": "10 Days"
    }
    ]
}
```

<p align="center">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
    <img src="http://ForTheBadge.com/images/badges/built-with-love.svg">
</p>
