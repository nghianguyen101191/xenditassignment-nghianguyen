import logging
import time

from utils import manage_util
from constants import constant
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import os
from PIL import Image
from io import BytesIO
from datetime import datetime


class ElementMethod:

    def __init__(self, locator):
        self.__strategies = {
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector
        }
        self.__locator = locator
        self.__dynamic_locator = locator

    @property
    def _driver(self):
        return manage_util.get_driver()

    @property
    def _element(self):
        return self.find_element()

    def find_element(self):
        prefix, criteria = self.__parse_locator(self.__locator)
        strategy = self.__strategies[prefix]
        return strategy(criteria)

    def __by(self, prefix):
        if prefix == "class":
            return By.CLASS_NAME
        elif prefix == "css":
            return By.CSS_SELECTOR
        else:
            return prefix

    def _find_by_xpath(self, criteria):
        return WebDriverWait(self._driver, constant.SEL_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, criteria)))

    def _find_by_css_selector(self, criteria):
        return WebDriverWait(self._driver, constants.SEL_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, criteria)))

    def click(self):
        self.wait_for_clickable()
        self._element.click()
        logging.info("Clicked element successfully " + str(self.__locator))

    def send_keys(self, *value):
        self._element.send_keys(value)
        logging.info("Send keys successfully " + str(self.__locator) + ". Key = " + str(value))

    def switch_to_iframe(self):
        self._driver.switch_to.frame(self.find_element())

    def switch_to_default_iframe(self):
        self._driver.switch_to.default_content()

    def send_keys_action(self, key_value):
        if str(key_value).upper() in constant.KEYS:
            key_value = constant.KEYS[str(key_value).upper()]
        actions = ActionChains(self._driver)
        actions.send_keys(key_value).perform()

    def wait_for_clickable(self, timeout=None):
        if timeout is None:
            timeout = constant.SEL_TIMEOUT
        prefix, criteria = self.__parse_locator(self.__locator)
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable((self.__by(prefix), criteria)))

    def take_screenshot(self):
        x = int(self._element.location["x"])
        y = int(self._element.location["y"])
        w = int(self._element.size["width"])
        h = int(self._element.size["height"])
        scr_img_canas = self._driver.get_screenshot_as_png()
        scr_img_canas = Image.open(BytesIO(scr_img_canas))
        #This is ratio in equal result box in FullScreenMode:https://www.online-calculator.com/html5/online-calculator/index.php?v=10
        scr_img_canas = scr_img_canas.crop((x * 2.5, y + x / 3.2, x * 3.85 + w, y + h / 3.8))
        now_date = datetime.now()
        image_path = "./image_save/" + str(now_date).replace(" ", "") + ".png"
        scr_img_canas.save(image_path, format='PNG')
        return image_path
