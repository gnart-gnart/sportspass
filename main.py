from dotenv import load_dotenv
from selenium import webdriver
import os
from driver import *
import time

driver = webdriver.Chrome()
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

driver.get("https://howdy.tamu.edu")

if not waitForPageToLoad(driver):
    driver.quit()
    exit()

interactWithElement(driver, By.ID, "loginbtn", "click")
interactWithElement(driver, By.ID, "username", "send_keys").send_keys(username)
interactWithElement(driver, By.ID, "password", "send_keys").send_keys(password)
interactWithElement(driver, By.ID, "password", "submit")
interactWithElement(driver, By.ID, "trust-browser-button", "click")

interactWithElement(driver, By.ID, "Pluto_31_u31l1n125_215616_webSearchInput", "send_keys").send_keys("sports pass")
interactWithElement(driver, By.ID, "Pluto_31_u31l1n125_215616_webSearchInput", "submit")

if not waitForPageToLoad(driver):
    driver.quit()
    exit()

driver.get("https://howdy.tamu.edu/uPortal/f/my-dashboard#SportsPass")
button = waitForElement(driver, By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div[3]/div/div/section/div[2]/div[2]/div/common-db-error-ui/dashboard-ui/div/mat-drawer-container/mat-drawer-content/div/div/sports-pass-ui//div/div/div[1]/div/button")
if button:
    button.click()
else:
    print("Failed to find that darn button")

# driver.quit()
