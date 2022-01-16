
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import projectConfig

PATH = "/usr/bin/chromedriver"
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'log.txt')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)

driver = webdriver.Chrome(PATH)

login = projectConfig.login

driver.get("http://google.com")
pesquisa = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > input")
pesquisa.click()
pesquisa.send_keys("teste")

pesquisa.send_keys(Keys.ENTER)
