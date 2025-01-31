from selenium.webdriver.support import expected_conditions as EC
from base_elements.base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait as wait


class Input(BaseElement):
    def send_keys(self, locator,  keys: str):
        element = wait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(keys)
