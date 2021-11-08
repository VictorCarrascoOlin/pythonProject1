# importing necessary module for Selenium Python tutorial
import pytest
from selenium import webdriver
import sys
from time import sleep
from selenium.webdriver.chrome.service import Service


#s = Service("drivers/chromedriver.exe")


# Initiating ChromeDriver for this Selenium Python Tutorial
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome("drivers/chromedriver.exe")
    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    chrome_driver.find_element_by_name("li1").click()
#    chrome_driver.find_element(by="Li1").click()
    chrome_driver.find_element_by_name("li2").click()
#    chrome_driver.find_element(by="Li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element_by_id("sampletodotext")
#    email_text_field = chrome_driver.find_element(by="sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    chrome_driver.find_element_by_id("addbutton").click()
    sleep(5)

    output_str = chrome_driver.find_element_by_name("li6").text
#    output_str = chrome_driver.find_element(by="Li6").text
    sys.stderr.write(output_str)

    sleep(2)
    chrome_driver.close()
