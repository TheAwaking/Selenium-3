from base.base_page import BasePage
from selenium.webdriver.common.by import By

from base_elements.Input import Input
from base_elements.button import Button
from base_elements.web_element import WebElement
from utils.url_utils import add_basic_auth_to_url


class LogInPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials.')]")
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.ID, "content")

    def __init__(self, driver):
        super().__init__(driver)
        self.auth_button = Button(driver, self.AUTH)
        self.page = WebElement(driver, self.UNIQUE_ELEMENT_LOC)
        self.credential_alert = WebElement(driver, self.CRED)

    def click_auth_button(self):
        self.auth_button.click()

    def check_auth_page(self):
        self.page.visibility_of_element_located()

    def validate_credentials(self):
        alert_element = self.credential_alert.visibility_of_element_located()
        return alert_element.text

    # def cred_alert(self, base_url, username, password):
    #     auth_url = add_basic_auth_to_url(base_url, username, password)
    #     self.driver.get(auth_url)
