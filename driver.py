from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def waitForElement(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

def findElement(driver, by, value):
    return driver.find_element(by, value)

def interactWithElement(driver, by, value, action='click'):
    if by == By.XPATH and 'href' in value:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((by, f'//a[@href="{value}"]'))
        )
    else:
        element = waitForElement(driver, by, value)
    
    if action == 'click':
        element.click()
    elif action == 'send_keys':
        return element
    elif action == 'submit':
        element.send_keys(Keys.RETURN)
    
    return element
