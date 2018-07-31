import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get ("https://www.cleartrip.com/")
time.sleep(10)
assert "Search flights" in driver.page_source
time.sleep(5)
driver.find_element_by_name("origin").send_keys("Chennai")
time.sleep(5)
driver.find_element_by_partial_link_text("Chennai").click()
time.sleep(2)
driver.find_element_by_name("destination").send_keys("Pune")
time.sleep(5)
driver.find_element_by_partial_link_text("Pune").click()
time.sleep(5)
driver.find_element_by_link_text("15").click()
time.sleep(5)
driver.find_element_by_id("SearchBtn").click()
time.sleep(5)
