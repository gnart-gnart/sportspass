from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def waitForElement(driver, by, value, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Timeout while waiting for element with {by}='{value}'")
        return None

def interactWithElement(driver, by, value, action='click'):
    element = waitForElement(driver, by, value)
    if element:
        try:
            if action == 'click':
                WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((by, value))
                ).click()
            elif action == 'send_keys':
                return element
            elif action == 'submit':
                element.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Failed to {action} element with {by}='{value}': {e}")
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
