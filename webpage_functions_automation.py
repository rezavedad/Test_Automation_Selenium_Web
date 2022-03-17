from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
time.sleep(5)
driver.get("https://www.google.com/")

# Locate Elements
#driver.find_element_by_name("q").send_keys("iphone 14")
#driver.find_element_by_name("btnK").click()
