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


sportsPassSecured = False

while not sportsPassSecured:
    if not waitForPageToLoad(driver):
        driver.quit()
        exit()
    
    # Do funky stuff because the "Click here to view sports pass" button is in a shadow DOM
    try:
        sports_pass_ui = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "sports-pass-ui"))
        )
        print("Found sports-pass-ui element.")
    except Exception as e:
        print("Failed to find sports-pass-ui element:", e)
        driver.quit()
        exit()

    time.sleep(1)
    shadow_root = None
    for _ in range(5):  # Try up to 5 times
        try:
            shadow_root = driver.execute_script('return arguments[0].shadowRoot', sports_pass_ui)
            if shadow_root:
                print("Successfully accessed the shadow DOM.")
                break
            else:
                print("Shadow DOM not ready yet, retrying...")
                time.sleep(1)
        except Exception as e:
            print("Error accessing shadow DOM, retrying:", e)
            time.sleep(1)

    if not shadow_root:
        print("Failed to access the shadow DOM after multiple attempts.")
        driver.quit()
        exit()

    try:
        button = WebDriverWait(shadow_root, 20).until(
            lambda shadow: shadow.find_element(By.CSS_SELECTOR, "button")
        )
        if "Sports Pass" in button.text:
            print("Found the button inside the shadow DOM.")
    except Exception as e:
        print("Failed to find the button inside the shadow DOM:", e)
        driver.quit()
        exit()

    try:
        button.click()
        print("Clicked the button successfully.")
    except Exception as e:
        print("Failed to click the button:", e)

    # Now click the ""
    radio_input = waitForElement(shadow_root, By.CSS_SELECTOR, "input[type='radio'][id='option1']")
    if radio_input.is_enabled():
        radio_input.click()

        # Find the save button and try to click it
        # Do Funky Stuff CLick save my choice button
        try:
            sports_pass_ui = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "sports-pass-ui"))
            )
            print("Found sports-pass-ui element.")
        except Exception as e:
            print("Failed to find sports-pass-ui element:", e)
            driver.quit()
            exit()

        time.sleep(1)
        shadow_root = None
        for _ in range(5):  # Try up to 5 times
            try:
                shadow_root = driver.execute_script('return arguments[0].shadowRoot', sports_pass_ui)
                if shadow_root:
                    print("Successfully accessed the shadow DOM.")
                    break
                else:
                    print("Shadow DOM not ready yet, retrying...")
                    time.sleep(1)
            except Exception as e:
                print("Error accessing shadow DOM, retrying:", e)
                time.sleep(1)

        if not shadow_root:
            print("Failed to access the shadow DOM after multiple attempts.")
            driver.quit()
            exit()

        try:
            button = WebDriverWait(shadow_root, 20).until(
                lambda shadow: shadow.find_element(By.CSS_SELECTOR, "button")
            )
            if "Save" in button.text:
                print("Found the save my choice button inside the shadow DOM.")
        except Exception as e:
            print("Failed to find the save my choice button inside the shadow DOM:", e)
            driver.quit()
            exit()

        try:
            button.click()
            print("Clicked the save my choice button successfully.")
            sportsPassSecured = True
        except Exception as e:
            print("Failed to click the save my choice button:", e)


            
    else:
        print("Input is disabled, refreshing and restarting the process...")
        driver.refresh()

# Close the driver
driver.quit()
