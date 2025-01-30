from base.base_page import BasePage
from selenium.webdriver.common.by import By
from base_elements.base_element import BaseElement


class LogInPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//button[@type='password']")
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.XPATH, "//div[@id='content']")

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.base_element = BaseElement(driver, timeout)

    def click_auth_button(self):
        self.base_element.element_is_clickable(self.AUTH).click()

    def validate_credentials(self):
        alert_element = self.base_element.visibility_of_element_located(self.CRED)
        return alert_element.text
