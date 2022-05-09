from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver .common.action_chains import  ActionChains


s=Service("C:\BrowserWindows\Newchrome\chromedriver.exe")
driver=webdriver.Chrome (service=s)
driver.implicitly_wait(20)
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element(By.CLASS_NAME ,"wikipedia-search-input").send_keys("soft")
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
search_ele=driver.find_elements(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-results']//div//a")

print(len(search_ele ))
for element in search_ele :
    print (element.text )
    if element.text == "Software testing":
        element.click()
        break