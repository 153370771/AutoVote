import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from random import Random

def random_str(randomlength=40):
    str = ''
 
    chars = 'AaBbCcDdEeFf0123456789'
 
    length = len(chars) - 1
 
    random = Random()
 
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
 
    return str

for i in range(1000):
	ethaddress='0x'+random_str()
	browser=webdriver.Firefox()
	browser.get("https://yeecall.gl.yeecall.com/activity/share?t=5a59f822e07d103698f99447")

	browser.find_element_by_name('address').send_keys(ethaddress) # 自动敲入用户名
	browser.find_element_by_css_selector("button").click() # 点击“账户登录”
	time.sleep(1)
	browser.close()