import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get ("https://www.cleartrip.com/")
time.sleep(10)
driver.find_element_by_link_text("Hotels").click()
time.sleep(5)
assert "Search for hotels" in driver.page_source
time.sleep(5)
driver.find_element_by_id("Tags").send_keys("Indiranagar, Bangalore")
time.sleep(5)
driver.find_element_by_partial_link_text("Indiranagar, Bangalore").click()
driver.find_element_by_id("SearchHotelsButton").click()