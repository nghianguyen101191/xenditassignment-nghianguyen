from webdriver_manager.chrome import ChromeDriverManager
from constants import constant
from selenium import webdriver

class Driver:
    def __init__(self):
        self._driver = None

    def create_driver(self, browser_name="chrome"):
        if browser_name.lower() == "chrome":
            return self.init_chrome_browser()
        else:
            print('Implement Later')

    def init_chrome_browser(self):
        if constant.CHROME_VERSION is not None:
            self._driver = webdriver.Chrome(executable_path=ChromeDriverManager(constants.CHROME_VERSION).install())
        else:
            self._driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self._driver.implicitly_wait(constant.SEL_TIMEOUT)
        return self._driver