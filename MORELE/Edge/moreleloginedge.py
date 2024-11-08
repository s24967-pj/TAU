from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
import time


class WrongEmail:
    
    logging.basicConfig(filename='./TauMoreleTestLoginEdge.log', filemode='w', level=logging.DEBUG)
    logger = logging.getLogger('Selenium TAU Lab2 - Morele')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)

    driver.get('https://www.morele.net/')

    logger.info("Opening https://www.morele.net/...")

    assert "Morele" in driver.title, "The title of the page does not contain 'Morele'."
    assert driver.current_url == 'https://www.morele.net/', "URL does not match expected Morele homepage URL."

    driver.maximize_window()


    time.sleep(1)

    try:
        cookies_XPATH = "/html/body/div[5]/div/dialog/div/div/div[3]/button[3]"
        element = driver.find_element(By.XPATH, cookies_XPATH)
        logger.info(f"CLICKING COOKIES")
        assert element.is_displayed(), "'Accept cookies' button is not displayed."
        assert element.is_enabled(), "'Accept cookies' button is not clickable."
        element.click()

    except:
        logger.error("Unable to accept cookies")

    time.sleep(2)

    try:
        login_XPATH = "/html/body/div[2]/div/header/div/div/div/div[2]/div/div[2]/div/div[4]/button/span"
        element = driver.find_element(By.XPATH, login_XPATH)
        logger.info("Opening login tab...")

        element.click()
        time.sleep(1)

        login_modal_XPATH = "/html/body/main/div/div/div[3]/form"
        login_modal = driver.find_element(By.XPATH, login_modal_XPATH)
        assert login_modal.is_displayed(), "Login form did not display after clicking login button."

    except:
        logger.error("Unable to get to Login tab")


    time.sleep(1)
    
    try:
        email_XPATH = "/html/body/main/div/div/div[3]/form/div[1]/input"
        username = driver.find_element(By.XPATH, email_XPATH)
        logger.info("Input wrong email...")
        username.click()
        username.send_keys("TEST@wp.pl")
        email_value = username.get_attribute("value")
        assert "@" in email_value and "." in email_value, "Email format is incorrect."
    except:
        logger.error("Unable to type email")


    try:
        password_XPATH = "/html/body/main/div/div/div[3]/form/div[2]/input"
        password = driver.find_element(By.XPATH, password_XPATH)
        logger.info("Input test password...")
        assert password.is_displayed(), "Password input field is not displayed."
        password.click()
        password.send_keys("TEST")

    except:
        logger.error("Unable to type password")

    time.sleep(2)

    try:
        button_XPATH = "/html/body/main/div/div/div[3]/form/button"
        element = driver.find_element(By.XPATH, button_XPATH)
        logger.info("Trying to login...")
        assert element.is_displayed(), "Login button is not displayed."
        assert element.is_enabled(), "Login button is not clickable."
        element.click()
    except:
        logger.error("Unable to click login")

    time.sleep(2)

    try:
        element = driver.find_element(By.CLASS_NAME, "mn-body")
        logger.info("Test was completed successfuly")
    except:
        logger.critical("Could not find error message")

    driver.close()
    driver.quit()
