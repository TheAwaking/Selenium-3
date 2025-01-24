from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:

    def __init__(self, driver):
        self.driver = driver

    def element_is_clickable(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def visibility_of_element_located(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
