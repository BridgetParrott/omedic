#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:11:06 2021

@author: alan
"""



import gender_guesser.detector as gender
from selenium import webdriver
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
import logging.config
import os
import sys
import unidecode
import six
import pause
import argparse
import logging.config
import re
import time
import random
import json
from dateutil import parser as date_parser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from Sender import *




LOGGER = logging.getLogger()
orthinURL = "http://resultados.orthinlab.com.mx:8888/lab/request-entry/#/login"
adminURL = "https://omedic.com.mx/admin/"
SUBMIT_BUTTON_XPATH = "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[6]/button"
username = '22268'
password = '123456'
# instalando el web driver de chrome mas reciente e instanciandolo
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)


try:
    LOGGER.info("Requesting page: " + orthinURL)
    driver.get(orthinURL)
except TimeoutException:
    LOGGER.info("Page load timed out but continuing anyway")

LOGGER.info("Waiting for login fields to become visible")

LOGGER.info("Entering username and password")
email_input = driver.find_elements_by_id("inputUserName")
#email_input.clear()
email_input.send_keys(username)

password_input = driver.find_element_by_id("inputPassword")
password_input.clear()
password_input.send_keys(password)

LOGGER.info("Logging in")
driver.find_element_by_xpath("//button[@type='button']").click()

LOGGER.info("Successfully logged in")


driver.find_element_by_xpath("//li[@class='slab-app-sidebar-button ng-star-inserted selected']").click()
driver.find_element_by_xpath("//i[@class='icon-context-menu']").click()
driver.find_element_by_xpath("//a[@class='slab-flex-1']").click()


  

