from selenium import webdriver
import time
from dotenv import load_dotenv
import os

def wait():
    time.sleep(0.25)

# Initialization
driver = webdriver.Chrome()
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Login to Howdy
driver.get("https://howdy.tamu.edu")
wait()
driver.find_element_by_id("loginbtn").click()
wait()
driver.find_element_by_id("username").sendKeys(username)
wait()
driver.find_element_by_id("password").sendKeys(password)
wait()

# Close the WebDriver
driver.quit()
