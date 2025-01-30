import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import config


class BaseElement:
    DEFAULT_WAIT_TIME = 20

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.wait = wait(driver, timeout)
        self.timeout = timeout if timeout is not None else BaseElement.DEFAULT_WAIT_TIME

    def element_is_clickable(self, locator):
        return wait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def visibility_of_element_located(self, locator):
        return wait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
