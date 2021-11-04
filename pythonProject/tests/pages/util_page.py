import logging

from utils import manage_util


class UtilPage:
    def __init__(self):
        self.driver = manage_util.get_driver()
        if self.driver is None:
            manage_util.start_driver()
            manage_util.maximize_browser()
            self.driver = manage_util.get_driver()

    def open_url(self, url):
        self.driver.get(url)
        logging.info("Open Page properly" + url)

    def close_browser(self):
        self.driver.close_browser()
