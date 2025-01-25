from base.base_page import PageBase
from selenium.webdriver.common.by import By
from base_elements.base_element import BaseElement


class LogInPage(PageBase, BaseElement):
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.XPATH, "//div[@id='content']")

    def __init__(self, driver):
        super().__init__(driver)

    def basic_auth(self):
        self.element_is_clickable(self.AUTH).click()

    def validate_credentials(self):
        alert_element = self.visibility_of_element_located(self.CRED)
        return alert_element.text
