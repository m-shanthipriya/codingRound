import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
SITE_URL="https://www.cleartrip.com/"

def signInSuccess():
    driver.get (SITE_URL)
    time.sleep(10)
    driver.find_element_by_id("userAccountLink").click()
    driver.find_element_by_id("SignIn").click()
    driver.switch_to.frame("modal_window")
    time.sleep(10)
    driver.find_element_by_id("email").send_keys("sampleemail@gmail.com")
    driver.find_element_by_id("password").send_keys("password")
    driver.find_element_by_id("signInButton").click()
    driver.close()

def signInFailureWithoutGivingCredential():
    driver.get (SITE_URL)
    time.sleep(10)
    driver.find_element_by_id("userAccountLink").click()
    driver.find_element_by_id("SignIn").click()
    driver.switch_to.frame("modal_window")
    time.sleep(10)
    driver.find_element_by_id("signInButton").click()
    assert "There were errors in your submission" in driver.page_source
    driver.close()
    
signInSuccess()
signInFailureWithoutGivingCredential()
