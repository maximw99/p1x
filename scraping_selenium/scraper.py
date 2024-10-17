from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Firefox()


driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
driver.find_element(By.XPATH, "//div[text()='Accept all']").click()

input_element.send_keys('moerfelden walldorf wochenmarkt' + Keys.ENTER)

time.sleep(10)

driver.quit()