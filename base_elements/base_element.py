from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    DEFAULT_WAIT_TIME = 20

    def __init__(self, driver, locator, timeout=None):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout if timeout is not None else BaseElement.DEFAULT_WAIT_TIME
        self.wait = WebDriverWait(driver, self.timeout)

    def element_is_clickable(self):
        return self.wait.until(EC.element_to_be_clickable(self.locator))

    def visibility_of_element_located(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator))

    def element_is_present(self):
        return self.wait.until(EC.presence_of_element_located(self.locator))

    def click(self):
        element = self.element_is_clickable()
        element.click()

    def get_text(self):
        element = self.visibility_of_element_located()
        return element.text
