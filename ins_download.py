from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

# wait until html elements are loaded
def wait():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        pass

# download a single video by url, save it as 'root/id.mp4'
def downloadVideo(url,root,id):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    path = root +'/'+ str (id) +'.mp4'
    print(path)

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=headers)
            print(r.status_code)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
    print()


# parser: retrieve video download url from html text
def get_video_url(text):
    p = text.find('video_url')
    if p!=-1:
        st = p+12
        ed = text.find('\"',st+1)
        if ed == -1 or ed <= st:
            return ''
        return text[st:ed]
    else:
        return ''


# explore a certain tag and download a certain number of videos
# 1. scroll down till the video number is enough or no more posts
# 2. get video_download_url by requests and parser
# 3. download single videos
def search_tag_and_download_videos(tag = 'cat' , num_videos = 10, root = None):
    if root == None:
        root = tag
    url = f'https://www.instagram.com/explore/tags/{tag}/'
    driver.get(url)

    wait()
    linklist = []
    last = ''
    cnt = 0
    while(len(linklist)<=num_videos):

        print(f'{len(linklist)}/{num_videos} links acquired')

        ls = driver.find_elements_by_xpath("//span[@aria-label='视频']/../..")


        try:
            top_link = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a[1]")[9].get_attribute('href')
            if top_link == last:
                cnt += 1
            else:
                last = top_link
                cnt = 0
        except:
            cnt += 1
            last = ''
            pass


        for item in ls:
            try:
                link = item.get_attribute('href')
                if link not in linklist:
                    linklist.append(link)
            except:
                pass

        if cnt >= 5:
            print(f"\nOnly {len(linklist)} videos is qualified\n")
            break

        for i in range(20):
            driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
            time.sleep(0.1)
        time.sleep(5)

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    print(f'Start downloading: {len(linklist)} videos\n')

    for i in range(len(linklist)):

        link = linklist[i]

        print(f'{i}/{len(linklist)} videos')
        time.sleep(1)

        cookies = driver.get_cookies()
        s = requests.Session()
        id = link.split('/')[-2]
        link += '?__a=1'
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])
        r = s.get(link+'',headers=headers)
        url = get_video_url(str(r.text))
        if url != '':
            downloadVideo(url,root,id)

    driver.close()
    return


def login(username,password):
    login_url = 'https://www.instagram.com/accounts/login/'
    driver.get(login_url)
    wait()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
    wait()

import argparse
parser = argparse.ArgumentParser(description="Kwai_download_args")
parser.add_argument('--tag','-t',default='cat')
parser.add_argument('--num','-n',type=int, default=10)
parser.add_argument('--username','-u')
parser.add_argument('--password','-p')
parser.add_argument('--root','-r',default=None)
args=parser.parse_args()


if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # Do not use the same account on different devices in parallel, which risks being banned, too.
    login(args.username,args.password)

    search_tag_and_download_videos(tag = args.tag, num_videos = args.num, root = args.root)