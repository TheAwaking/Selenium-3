from base.base_page import PageBase
from selenium.webdriver.common.by import By
from base_elements.base_element import BaseElement


class LogInPage(BaseElement, PageBase):
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.XPATH, "//p[contains(text(), 'Congratulations!')]")

    def __init__(self, driver):
        super().__init__(driver)

    def basic_auth(self):
        self.element_is_clickable(self.AUTH).click()

    def validate_credentials(self):
        self.visibility_of_element_located(self.CRED)
