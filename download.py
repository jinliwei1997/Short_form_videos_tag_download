from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import requests


def wait():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        pass

def downloadVideo(url,root,id):

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    path = root +'\\'+ str (id) +'.mp4'
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

def search_tag_and_download_videos(tag = 'cat' , num_videos = 10 ):
    url = f'https://www.instagram.com/explore/tags/{tag}/'
    driver.get(url)

    wait()
    linklist = []
    while(len(linklist)<num_videos):
        print(len(linklist))
        ls = driver.find_elements_by_xpath("//span[@aria-label='视频']/../..")

        for item in ls:
            try:
                link = item.get_attribute('href')
                if link not in linklist:
                    linklist.append(link)
            except:
                pass
        for i in range(20):
            driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
            time.sleep(0.1)
        time.sleep(5)

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }
    for link in linklist:
        cookies = driver.get_cookies()
        s = requests.Session()
        id = link.split('/')[-2]
        link += '?__a=1'
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])
        r = s.get(link+'',headers=headers)
        url = get_video_url(str(r.text))
        if url != '':
            downloadVideo(url,tag,id)

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

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # Please use your own account to avoid being banned by instagram.
    # Do not use the same account on different devices in parallel, which risks being banned, too.
    username = 'jinliwei1998'
    password = 'jlw260817'

    login(username,password)

    search_tag_and_download_videos()