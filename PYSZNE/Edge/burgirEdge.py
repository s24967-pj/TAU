import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='./TauBurgerTestEdge.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger('Selenium TAU Lab2 - pyszne')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

logger.info("Opening Burger King homepage")
driver.get('https://burgerking.pl/pl/')

assert "Burger King" in driver.title, "Page title does not contain 'Burger King'."

driver.maximize_window()

time.sleep(3)

try:
    cookies_xpath = "/html/body/div[4]/div[2]/div/div/div[3]/button"
    cookies = driver.find_element(By.XPATH, cookies_xpath)
    cookies.click()
    assert cookies.is_displayed(), "Cookies consent button is not displayed."
    assert cookies.is_enabled(), "Cookies consent button is not enabled."
    logger.info("cookies closed")
except:
    logger.error("Unable to close cookies")

time.sleep(2)

try:
    menu_xpath = "/html/body/div[1]/div/div[1]/div[2]/button/span"
    menu = driver.find_element(By.XPATH, menu_xpath)
    assert menu.is_displayed(), "Menu button is not displayed."
    assert menu.is_enabled(), "Menu button is not clickable."
    menu.click()
except:
    logger.error("Unable to go to menu")

time.sleep(2)

try:
    language_xpath = "/html/body/reach-portal/div[2]/div/div/div/div/div/div/div[1]/div[2]/label/span"
    english_option = driver.find_element(By.XPATH, language_xpath)
    assert english_option.is_displayed(), "English language option is not displayed."
    assert english_option.is_enabled(), "English language option is not clickable."
    english_option.click()
    logger.info("changing language")
except:
    logger.error("Unable to choose change language")

time.sleep(1)

try:
    accept_xpath = "/html/body/reach-portal/div[2]/div/div/div/div/div/div/div[2]/div/button"
    element = driver.find_element(By.XPATH, accept_xpath)
    assert element.is_displayed(), "Language change confirmation button is not displayed."
    assert element.is_enabled(), "Language change confirmation button is not clickable."
    element.click()
    logger.info("approve changing language")
    
    time.sleep(1)
    
    assert "https://burgerking.pl/en/" in driver.current_url, "URL does not contain '/en/'"
    logger.info("Correct URL, test passed")
except AssertionError as e:
    logger.error("URL is incorrect: %s", e)
except Exception as e:
    logger.error(f"Error during language confirmation: {e}")

time.sleep(2)

driver.close()
driver.quit()
