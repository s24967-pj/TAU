import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(filename='./TauOpggTestLeaderboardChrome.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger('Selenium TAU Lab2 - OPGG')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome()

logger.info('Opening OP.GG site on european server')
driver.get('https://www.op.gg/')

assert "OP.GG" in driver.title 


initial_window_size = driver.get_window_size()
driver.maximize_window()
maximized_window_size = driver.get_window_size()
assert maximized_window_size != initial_window_size, "Window size did not change after maximizing"

logger.info("Trying to click on Leaderboards")

try:
    xpath = "/html/body/div[1]/div/div/div/div[2]/div/button[2]"
    element = driver.find_element(By.XPATH, xpath)
    logger.info(f"CLICKING COOKIES")

    element.click()

    xpath = "/html/body/div[2]/header/div[3]/nav/ul[1]/li[4]/a"
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    assert element.is_displayed(), "Leaderboards button not displayed"
    logger.info("Going into Leaderboards")
except:
    logger.error("Unable to get to Leaderboards tab")


time.sleep(5)
logger.info("Trying to get first place summoner name")

try:
    player_xpath = "//body//div//div//div//table//tbody/tr[1]/td[2]//div/span[1]"
    temp = driver.find_element(By.XPATH, player_xpath)
    logger.info("Player: %s", temp.text)
except:
    logger.error("Unable to get first place summoner name")

try:
    points_xpath = "//body//div//div//div//table//tbody/tr[1]/td[4]/span"
    temp = driver.find_element(By.XPATH, points_xpath)
    logger.info("Points: %s", temp.text)
except:
    logger.error("Unable to get first place summoner points")

driver.close()