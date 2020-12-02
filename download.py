from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

# Please use your own account to avoid being banned by instagram.
# Do not use the same account on different devices in parallel, which risks being banned, too.
username = 'jinliwei1998'
password = 'jlw260817'


def downloadVideo(root,id):
    url = driver.find_element_by_xpath("//video[1]").get_attribute("src")
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
    return


if __name__ == '__main__':
    tag = 'cat'
    login_url = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(3)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
    time.sleep(3)

    url = 'https://www.instagram.com/p/CISZ4HUJkxa/'
    driver.get(url)
    downloadVideo('cat','CISZ4HUJkxa')




