import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from random import Random

#自动生成40位长度的16进制字符串
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
	browser_bin = os.path.join("C:/Users/wlw93/Desktop/", "chromedriver.exe")
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument("--disable-notifications")
	chrome_options.add_argument("--enable-automation")
	browser = webdriver.Chrome(browser_bin, chrome_options=chrome_options)
	browser.get("https://yeecall.gl.yeecall.com/activity/share?t=5a59f822e07d103698f99447")

	browser.find_element_by_name('address').send_keys(ethaddress)
	browser.find_element_by_css_selector("button").click() ”
	time.sleep(1)
	browser.close()