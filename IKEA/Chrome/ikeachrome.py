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

assert "IKEA" in driver.title, "IKEA site title is incorrect"

driver.maximize_window()

time.sleep(2)


try:
    meble_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/a/div"
    element = driver.find_element(By.XPATH, meble_xpath)
    assert element.is_displayed(), "'MEBLE' is not displayed"
    assert element.is_enabled(), "'MEBLE' is not clickable"
    logger.info(f"CLICKING MEBLE")
    element.click()
except:
    logger.error("'MEBLE' NOT OK")

try:
    sofa_xpath = "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/ul[2]/li[1]/a"
    element = driver.find_element(By.XPATH, sofa_xpath)
    assert element.is_displayed(), "'Sofy i narożniki' is not displayed"
    assert element.is_enabled(), "'Sofy i narożniki' is not clickable"
    logger.info(f"CLICKING 'sofy i narozniki''")
    element.click()
except:
    logger.error("choosing 'sofy i narozniki' NOT OK")

time.sleep(1)

logger.info("Clicking on product")

try:
    product_xpath = "/html/body/main/div[5]/div[1]/div[2]/section/div[2]/div[1]/div/div[3]/a/div[1]/div[1]/h3/span[1]/span"
    element = driver.find_element(By.XPATH, product_xpath)
    assert element.is_displayed(), "Product is not displayed"
    assert element.is_enabled(), "Product is not clickable"
    logger.info(f"Product clicked")
    element.click()
except:
    logger.error("cannot show product")

time.sleep(1)

logger.info("Adding to cart")

try:
    adding_xpath = "/html/body/main/div/div[1]/div/div[2]/div[2]/div[2]/div[6]/div/div/div/button/span/span"
    element = driver.find_element(By.XPATH, adding_xpath)
    logger.info(f"Added to cart'")
    element.click()
except:
    logger.error("cannot add to cart")

time.sleep(1)

logger.info("Going to cart")

try:
    heart_xpath = "/html/body/div[15]/div/div[3]/div/div[3]/button[2]/span"
    element = driver.find_element(By.XPATH, heart_xpath)
    logger.info(f"CLICKING CART")
    element.click()
except:
    logger.error("CART NOT OK")

time.sleep(1)

try:
    cost_xpath = "/html/body/main/main/div/div/div[31]/div/div[1]/div/div[2]/span/span[1]/span[1]/span[2]"
    temp = driver.find_element(By.CLASS_NAME, "cart-ingka-price__integer")
    cost_text = temp.text
    assert len(temp.text) > 0, "Cost is empty"
    assert cost_text.isdigit(), "Cost contains non-numeric characters"
    logger.info("KOSZT: %s", temp.text)
except:
    logger.error("Unable to get cost")
    assert False, "Unable to retrieve or validate cost"

driver.close()