from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH="C:\Program Files\chromedriver.exe"
net_addr = input("Enter the ip addres of web authenticator site : ")
uname = input("Enter Pfsense username : ")
password = input("Enter Pfsense password : ")

driver = webdriver.Chrome(PATH)
driver.get("https://"+ net_addr +"/")
driver.maximize_window()
buttonAdvanced = driver.find_element_by_xpath('//*[@id="details-button"]')
buttonAdvanced.click()
buttonProceed = driver.find_element_by_xpath('//*[@id="proceed-link"]')
buttonProceed.click()

# Sign in process;
uName = driver.find_element_by_xpath('//*[@id="usernamefld"]')
uName.send_keys(uname)

passwd = driver.find_element_by_xpath('//*[@id="passwordfld"]')
passwd.send_keys(password)
passwd.send_keys(Keys.RETURN)

linkServices = driver.find_element_by_xpath('//*[@id="pf-navbar"]/ul[1]/li[4]/a')
linkServices.click() # Services

linkCaptivePortal = driver.find_element_by_xpath('//*[@id="pf-navbar"]/ul[1]/li[4]/ul/li[2]/a')
linkCaptivePortal.click() # Captive Portal

linkEdit = driver.find_element_by_xpath('//*[@id="3"]/div/form/div/div[2]/table/tbody/tr/td[5]/a[1]')
linkEdit.click() # edit the captive portal configuration

changeLimit = driver.find_element_by_xpath('//*[@id="radiusperuserbw"]')
changeLimit.click() # change the target situation

buttonSave = driver.find_element_by_xpath('//*[@id="save"]')
buttonSave.click() # save & go back to the main page of captive portal

driver.close()
