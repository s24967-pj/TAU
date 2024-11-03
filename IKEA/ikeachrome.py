import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(filename='./TauIKEATestChrome.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger('Selenium TAU Lab2 - OPGG')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome()

logger.info('Opening ikea site')
driver.get('https://www.ikea.com/pl/pl/')



driver.maximize_window()

logger.info("Trying to click on favourites")

try:
    heart_xpath = "/html/body/header/div/ul/li[3]/a/span"
    element = driver.find_element(By.XPATH, heart_xpath)
    logger.info(f"CLICKING HEART")
    element.click()
except:
    logger.error("HEART NOT OK")

time.sleep(5)

driver.close()