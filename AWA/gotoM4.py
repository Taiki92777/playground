#%%
# access
from selenium import webdriver
import time
import sched
import re
from datetime import datetime

driver=webdriver.Chrome(rf'C:\Users\taiki\AppData\Local\Driver\chromedriver.exe')
driver.get('https://lib02.tmd.ac.jp/webclass/login.php')
#%%
# login
ID=driver.find_element_by_id('username')
ID.send_keys('#####')
password=driver.find_element_by_id('password')
password.send_keys('####')

login_button=driver.find_element_by_id('LoginBtn')
login_button.click()
#%%
M4_link=driver.find_element_by_xpath('//*[@id="%s"]/li[3]/div/div/a')
M4_link.click()
