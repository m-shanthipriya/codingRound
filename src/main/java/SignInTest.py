import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def sign_in_success():
    driver.get ("https://www.cleartrip.com/")
    time.sleep(10)
    driver.find_element_by_id("userAccountLink").click()
    driver.find_element_by_id("SignIn").click()
    driver.switch_to.frame("modal_window")
    time.sleep(10)
    driver.find_element_by_id("email").send_keys("sampleemail@gmail.com")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("signInButton").click()
    driver.close()
sign_in_success()

def sign_in_failure_without_giving_credential():
    driver.get ("https://www.cleartrip.com/")
    time.sleep(10)
    driver.find_element_by_id("userAccountLink").click()
    driver.find_element_by_id("SignIn").click()
    driver.switch_to.frame("modal_window")
    time.sleep(10)
    driver.find_element_by_id("signInButton").click()
    assert "There were errors in your submission" in driver.page_source
    driver.close()
sign_in_failure_without_giving_credential()
