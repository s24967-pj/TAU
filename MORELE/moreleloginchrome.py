from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
import time


class WrongEmail:
    
    logging.basicConfig(filename='./TauMoreleTestLoginChrome.log', filemode='w', level=logging.DEBUG)
    logger = logging.getLogger('Selenium TAU Lab2 - Morele')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    driver = webdriver.Chrome()

    driver.get('https://www.morele.net/')

    logger.info("Opening https://www.morele.net/...")

    driver.maximize_window()


    time.sleep(1)

    try:
        cookies_XPATH = "/html/body/div[5]/div/dialog/div/div/div[3]/button[3]"
        element = driver.find_element(By.XPATH, cookies_XPATH)
        logger.info(f"CLICKING COOKIES")
        element.click()

    except:
        logger.error("Unable to accept cookies")

    time.sleep(2)

    try:
        login_XPATH = "/html/body/div[2]/div/header/div/div/div/div[2]/div/div[2]/div/div[4]/button/span"
        element = driver.find_element(By.XPATH, login_XPATH)
        logger.info("Opening login tab...")

        element.click()

    except:
        logger.error("Unable to get to Login tab")


    time.sleep(1)
    
    try:
        email_XPATH = "/html/body/main/div/div/div[3]/form/div[1]/input"
        username = driver.find_element(By.XPATH, email_XPATH)
        logger.info("Input wrong email...")
        username.click()
        username.send_keys("TEST@wp.pl")

    except:
        logger.error("Unable to type email")


    try:
        password_XPATH = "/html/body/main/div/div/div[3]/form/div[2]/input"
        password = driver.find_element(By.XPATH, password_XPATH)
        logger.info("Input test password...")
        password.click()
        password.send_keys("TEST")

    except:
        logger.error("Unable to type password")

    time.sleep(2)

    try:
        button_XPATH = "/html/body/main/div/div/div[3]/form/button"
        element = driver.find_element(By.XPATH, button_XPATH)
        logger.info("Trying to login...")
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
