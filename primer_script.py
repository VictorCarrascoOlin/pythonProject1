from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)

driver.quit()



