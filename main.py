from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import *
import os

# Initialization
driver = webdriver.Chrome()
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Login to Howdy
driver.get("https://howdy.tamu.edu")
interactWithElement(driver, By.ID, "loginbtn", "click")
interactWithElement(driver, By.ID, "username", "send_keys").send_keys(username)
interactWithElement(driver, By.ID, "password", "send_keys").send_keys(password)
interactWithElement(driver, By.ID, "password", "submit")

# Trust the browser
interactWithElement(driver, By.ID, "trust-browser-button", "click")

# Navigate to sports pass page
interactWithElement(driver, By.ID, "Pluto_31_u31l1n125_215616_webSearchInput", "send_keys").send_keys("sports pass")
interactWithElement(driver, By.ID, "Pluto_31_u31l1n125_215616_webSearchInput", "submit")
interactWithElement(driver, By.XPATH, "/uPortal/f/my-dashboard#SportsPass", "click")
# Close the webdriver
# driver.quit()
