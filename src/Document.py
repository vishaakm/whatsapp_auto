from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import autoit
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
for name in names:
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
        #Click on attach
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header/div[3]/div/div[2]/div/span')))
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span').click()
        time.sleep(3)
        #Click on document
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]')))
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]').click()
        time.sleep(3)
        #Selecting the required file from path
        docPath = r'C:\Users\visha\PycharmProjects\Whatsapp\venv\res\Doc'
        autoit.win_wait_active("[Title:Open; Class:#32770]", 8)
        autoit.control_send("[Title:Open; Class:#32770]", "Edit1", docPath, 1)
        autoit.control_click("[Title:Open; Class:#32770]", "Button1")
        autoit.win_wait("[Title:Open; Class:#32770]", 5)
        autoit.control_focus("[Title:Open; Class:#32770]", "DirectUIHWND2")
        autoit.send("{CTRLDOWN}a")
        autoit.send("{CTRLUP}")
        autoit.send("{ENTER}")
        time.sleep(2)
        #Click send button
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span').click()
        time.sleep(3)

        log = 'Success'

