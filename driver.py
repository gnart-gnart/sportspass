from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def waitForElement(driver, by, value, timeout=30):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    except TimeoutException:
        print(f"Timeout while waiting for element with {by}='{value}'.")
        return None

def interactWithElement(driver, by, value, action='click'):
    element = waitForElement(driver, by, value)
    if element:
        if action == 'click':
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((by, value))
            ).click()
        elif action == 'send_keys':
            return element
        elif action == 'submit':
            element.send_keys(Keys.RETURN)
    else:
        print(f"Element with {by}='{value}' not found.")
    return element

def waitForPageToLoad(driver, timeout=30):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        return True
    except TimeoutException:
        print("Page load timed out.")
        return False
