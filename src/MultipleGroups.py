from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time

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

#Iterate through names
count = -1
for name in names:
    for number in numbers:
        #Submenu
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div')))
        driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
        time.sleep(2)
        #New Group
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]')))
        driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]').click()

        #Contact number
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/div[1]/div/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/div[1]/div/div/input').send_keys(str(number))
        time.sleep(1)

        #Number clicking
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/span').click()

        #Next clicking
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/span/div/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/span/div/span').click()
        time.sleep(2)

        #Type group subject
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/div[2]/div/div[2]/div[1]/div[2]')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/div[2]/div/div[2]/div[1]/div[2]').send_keys(name)
        time.sleep(2)

        #Submit the group
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/span/div/div/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/span/div/span/div/div/span/div/div/span').click()
        time.sleep(3)