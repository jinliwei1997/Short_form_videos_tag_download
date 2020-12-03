# Instagram_download
Download Instagram videos of a certain tag.

## TODO

~~filter out videos posts at tag searching page~~

~~replace Selenium browser implementation by Requests commands at the stage of downloading a single post~~

~~scroll down to acquire a certain number of video posts~~

---

write user guide

~~add process bar~~

~~fix the case that a certain tag does not own enough videos~~

## User Guide

1. Install selenium. For more details, please refer to [this link]([Selenium with Python中文翻译文档 — Selenium-Python中文文档 2 documentation (selenium-python-zh.readthedocs.io)](https://selenium-python-zh.readthedocs.io/en/latest/index.html)).
2. Install [Chrome Driver]([ChromeDriver - WebDriver for Chrome (chromium.org)](https://chromedriver.chromium.org/)) and add it to you system PATH.
3. Run this command:

```
python download.py -u <username> -p <password> -t <tag> -n <number>
```

For instance, use this line to download at least 10 (usually 10-20) videos from tag 'csgo'.

```
python download.py -u <username> -p <password> -t csgo -n 10
```

