<p align="center">
<img height="250px" src="https://raw.githubusercontent.com/arnoob16/cpAPI/master/cpApiLogo.png?token=ALWD5TNNXWTM4H3K3TVDSPLACQ4V6">
<h1 align="center">Competitive Programming API</h1>

<p align="center">
    An API built to give you updates about the upcoming contests on various Competitive Coding platforms.
</p>

</p>

---

<h3 align="center">Coding Platforms Supported</h3>

<p align="center">
    <img height="100px" src = "https://img.atcoder.jp/assets/atcoder.png"/>
    <img height="100px" src = "https://www.ime.usp.br/~arcjr/image/codeforces.png"/>
    <img height="100px" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXBUWY12NOXtKD9UEvtqkKeWAPyJm8GTkgEw&usqp=CAU"/>
    <img height="100px" src = "https://yt3.ggpht.com/ytc/AAUvwngkLcuAWLtda6tQBsFi3tU9rnSSwsrK1Si7eYtx0A=s900-c-k-c0x00ffffff-no-rj"/>
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
    - `startTime` => The starting timestamp of the contest.
    - `contestDuration` => The duration of the contest.

```
{
  "contests": [
    {
      "platform": "AtCoder",
      "contestName": "AtCoder Beginner Contest 189",
      "startTime": "2021-01-23T21:00:00",
      "contestDuration": "01:40 hours."
    },
    {
      "platform": "CodeForces",
      "contestName": "Codeforces Round #697 (Div. 3)",
      "startTime": "2021-01-25T14:35:00",
      "contestDuration": "02:00 hours."
    }
    ]
}
```

<p align="center">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
    <img src="http://ForTheBadge.com/images/badges/built-with-love.svg">
</p>
