from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import random
import time

user=input("Enter Your Instagram Username/Email :")
password=input("Enter Your Instagram Password :")
keyword=input("Enter the Username You Want to Get Search And Follow His/Her Followers:")
url="https://instagram.com"
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
usernm=driver.find_element(By.NAME,value="username")
usernm.send_keys(user)
time.sleep(2)
pas=driver.find_element(By.NAME,value="password")
pas.send_keys(password)
time.sleep(2)
login=driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(15)
notification=driver.find_element(By.CSS_SELECTOR,value="._a9-z button._a9_1").click()
time.sleep(5)
search_click=driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a').click()
time.sleep(10)
search_input=driver.find_element(By.CSS_SELECTOR,value="input[value='']")
search_input.send_keys(keyword)
time.sleep(5)
search_user=driver.find_elements(By.CSS_SELECTOR,value=".xocp1fn")
time.sleep(2)
suser=random.randint(0,len(search_user))
cuser=search_user[suser].click()
time.sleep(5)
tfollowers=driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span').text.replace(",",'')
try:
    click_followers=driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a').click()
except NoSuchElementException:
    pass
time.sleep(5)
followers=driver.find_elements(By.CSS_SELECTOR,value="div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3 button")
for f in range(int(tfollowers)):
    try:
        followers[f].click()
    except ElementClickInterceptedException:
        pass
    time.sleep(3)
time.sleep(10)