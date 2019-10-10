from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import bank_islam_credentials

browser = webdriver.Chrome("/mnt/d/Projects/bank_islam_monthly_status/chromedriver.exe")
browser.get("https://www.bankislam.biz")

browser.switch_to.frame("ribFrame")

internet_banking = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#linkLogin > div")))
internet_banking.click()

user_id = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
user_id.send_keys(bank_islam_credentials.USER_ID)

login_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#usernameForm > div:nth-child(4) > input")))
login_button.click()

checkbox = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#authImgWordAck")))
checkbox.click()


password = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
password.send_keys(bank_islam_credentials.PASSWORD)

login_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#submitAuth")))
login_button.click()

error = True
while error is True:
    try:
        account_summary = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shortcut-block > div > a:nth-child(2)")))
        account_summary.click()
        error = False
    except:
        frame = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "ribFrame")))
        browser.switch_to.frame(frame)

error = True
while error is True:
    try:
        balance = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#collapse > table > tbody > tr:nth-child(2) > th:nth-child(5)")))
        print("done1")
        balance = balance.text
        print(f"RM {balance}")
        error = False
    except:
        frame = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "ribFrame")))
        browser.switch_to.frame(frame)

print("OK all")
