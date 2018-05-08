from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from Log import *

#Driver
driver = webdriver.Chrome(r'res\chromedriver.exe')
driver.maximize_window()
driver.get('https://web.whatsapp.com')
wait = WebDriverWait(driver, 60)

#Read Contacts from Excel file
wb = openpyxl.load_workbook(r'res\info.xlsx')
sheet = wb['Employee Data']
names = []
numbers = []
for cellObj in sheet['B']:
    if cellObj.value != None:
        names.append(cellObj.value)
    else:
        pass
for cellObj in sheet['C']:
    if cellObj.value != None:
        numbers.append(cellObj.value)

#Wait for the site to load
time.sleep(5)

#Log object
logObj = Log()

#Iterate through names
for name in names:
    count = 0
    #Group name
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-chatlist-search"]')))
    searchGroup = driver.find_element_by_xpath('//*[@id="input-chatlist-search"]').send_keys(name)
    time.sleep(4)
    #Check if group is present or not
    if len(driver.find_elements_by_xpath('//*[@id="pane-side"]/div/div/span')) != 0:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div/div/span')))
        noContactFound = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/span').text
        log = 'Failed'
        if noContactFound == 'No chats, contacts or messages found':
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[2]/div/span/button/span')))
            driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/span/button/span').click()
            time.sleep(3)
    else:
        #Click on the existed group
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div/div/div/div[1]/div')))
        driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[1]/div').click()
        time.sleep(3)
        #Input the message
        with open(r'res\msg.txt',encoding='utf8') as msgFile:
            msg = msgFile.read()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
            time.sleep(2)
        #Send message
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/button/span')))
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button/span').click()
        time.sleep(3)
        log = 'Success'
        logObj.writeLog(name,0,log)
        count += 1



