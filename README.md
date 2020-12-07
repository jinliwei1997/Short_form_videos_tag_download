# Short_form_videos_tag_download
Download Instagram&Tiktok videos of a certain tag.

## User Guide

### Overview

This download tool is based on Selenium, a web browser simulator. It implements browser activities like 'typing username and password to login' and 'scroll the page down to view more items'. So **do not** close or minimize  the browser driver when the downloader is running.

As Instagram and Tiktok is not available in China Mainland, please check your network before starting to download videos.

### Requirements

1. Selenium. For more details, please refer to [this link]([Selenium with Python中文翻译文档 — Selenium-Python中文文档 2 documentation (selenium-python-zh.readthedocs.io)](https://selenium-python-zh.readthedocs.io/en/latest/index.html)).
2. [Chrome Driver]([ChromeDriver - WebDriver for Chrome (chromium.org)](https://chromedriver.chromium.org/)). Add it to your system PATH.
3. Requests.

### Instagram download

```
python download.py -u <username> -p <password> -t <tag> -n <number> -r <root>
```

Arguments:

- -u : Instagram username
- -p : Instagram password
- -t : search tag
- -n :  **(optional)** numbers of videos to download; default 10
- -r : **(optional)** download directory; default : search tag

For instance, use this line to download at least 10 videos from tag 'csgo' to './csgo_download'.

```
python download.py -u <username> -p <password> -t csgo -n 10 -r csgo_download
```

### Tiktok download

Under construction.