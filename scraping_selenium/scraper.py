from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


service = Service(executable_path="geckodrover")
driver = webdriver.Firefox(service=service)


driver.get("https://google.com")

time.sleep(10)

driver.quit()