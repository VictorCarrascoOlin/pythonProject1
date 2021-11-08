# Import the 'modules' that are required for execution

import sys
import time

import pytest
from selenium import webdriver


@pytest.mark.xfail
def test_chrome_url():
    web_driver = webdriver.Chrome("drivers/chromedriver.exe")
    web_driver.get("https://lambdatest.github.io/sample-todo-app/")

    web_driver.maximize_window()

    web_driver.find_element_by_name("li1").click()
    web_driver.find_element_by_name("li2").click()

    title = "Sample page - lambdatest.com"
    assert title == web_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = web_driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    time.sleep(5)

    web_driver.find_element_by_id("addbutton").click()
    time.sleep(5)

    output_str = web_driver.find_element_by_name("li6").text
    sys.stderr.write(output_str)
    time.sleep(2)
    web_driver.close()


@pytest.mark.xfail
def test_firefox_url():
    web_driver = webdriver.Firefox()
    web_driver.get("https://www.lambdatest.com/blog/")

    web_driver.maximize_window()

    title = "LambdaTest | A Cross Browser Testing Blog"
    assert title == web_driver.title
    time.sleep(2)
    web_driver.close()


@pytest.mark.skip
def test_safari_url():
    web_driver = webdriver.Safari()
    web_driver.get("https://www.lambdatest.com/")

    web_driver.maximize_window()

    title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
    assert title == web_driver.title
    time.sleep(2)
    web_driver.close()