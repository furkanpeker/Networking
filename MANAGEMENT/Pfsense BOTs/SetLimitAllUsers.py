import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# This program sets all users a speed limit given as input in freeRadius!

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


sLimit = input("Enter the speed limit (as Mbps) to be applied on freeRadius to all users : ")
strSLimit = str(sLimit)

#buttonMenu = driver.find_element_by_xpath('//*[@id="topmenu"]/div/div[1]/button')
#buttonMenu.click()

linkServices = driver.find_element_by_xpath('//*[@id="pf-navbar"]/ul[1]/li[4]/a')
linkServices.click() # Services

linkFreeRadius = driver.find_element_by_xpath('//*[@id="pf-navbar"]/ul[1]/li[4]/ul/li[10]/a')
linkFreeRadius.click() # FreeRadius

buttonMACS = driver.find_element_by_xpath('//*[@id="3"]/div/ul/li[2]/a')
buttonMACS.click() # MACS button


for i in range(0,287):
    buttonSelection = driver.find_element_by_xpath('//*[@id="mainarea"]/thead/tr[2]/td/select')
    buttonSelection.click() # selection

    buttonEdit = driver.find_element_by_xpath('//*[@id="id_'+ str(i) +'"]/td[9]/table/tbody/tr/td[1]/a')
    buttonEdit.click()

    description = driver.find_element_by_xpath('//*[@id="description"]')
    desc = description.text
    if((desc[-2:] == "pc") or (desc[-2:] == "Pc") or (desc[-2:] == "Tb") or (desc[-2:] == "tb") or (desc[-6:] == "Tablet")):
        continue
    else:
        valueSpeed = driver.find_element_by_xpath('//*[@id="varmacsmaxbandwidthdown"]')
        valueSpeed.clear()
        valueSpeed.send_keys(strSLimit)

        buttonSave = driver.find_element_by_xpath('//*[@id="submit"]')
        buttonSave.click()


driver.close
