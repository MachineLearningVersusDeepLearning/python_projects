#!/usr/bin/python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


binary_location = "/usr/bin/google-chrome"
driver_location = "/usr/local/bin/chromedriver"


option = webdriver.ChromeOptions()
option.binary_location = binary_location

driver = webdriver.Chrome(executable_path = driver_location,chrome_options=option)
driver.get("http://www.python.org")



assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
