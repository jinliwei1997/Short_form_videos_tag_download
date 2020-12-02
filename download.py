from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

# Please use your own account to avoid being banned by instagram.
# Do not use the same account on different devices in parallel, which risks being banned, too.
username = 'jinliwei1998'
password = 'jlw260817'

def wait():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        pass

def downloadVideo(link,root,id):
    driver.get(link)
    wait()
    try:
        url = driver.find_element_by_xpath("//video[1]").get_attribute("src")
        print('got a video')
    except:
        print(f'{link} is not a video.')
        return False;
    # url = 'https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f9f0000brm8f726tgqapf007a00&ratio=720p&line=0'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    }

    path = root +'\\'+ str (id) +'.mp4'
    print(path)

    try:
        if not os.path.exists(root):  #判断当前根目录是否存在
            os.mkdir(root)
        if not os.path.exists(path):
            #判断当前文件是否存在
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

def search_tag_and_download_videos(tag = 'cat' , num_videos = 10 ):
    url = f'https://www.instagram.com/explore/tags/cat/'

    driver.get(url)
    wait()
    ls = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a[1]")
    linklist = []
    for item in ls:
        link = item.get_attribute('href')
        if link not in linklist:
            linklist.append(link)

    for link in linklist:
        downloadVideo(link,tag,link.split('/')[-2])
    return




if __name__ == '__main__':
    tag = 'cat'
    login_url = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(login_url)

    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
    wait()

    search_tag_and_download_videos()



