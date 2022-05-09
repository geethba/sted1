from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

s=Service("C:\BrowserWindows\chromedriver.exe")
driver=webdriver.Chrome (service=s)
driver.implicitly_wait(20)
driver.get("https://www.goibibo.com/")
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("S")
autosuggestion_elements=driver.find_elements(By.XPATH ,'//ul[@id="react-autosuggest-1"]//li//div[@class="mainTxt clearfix"]//span')
print(len(autosuggestion_elements))
for element in autosuggestion_elements :
    print("list of suggestions:",element.text )
    if element.text== "Shirdi, India":
        print("element found")
        element.click()

        break