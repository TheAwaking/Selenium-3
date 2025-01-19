from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators
from base.page_base import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")



class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_basic_auth(self):
        self.wait.until(EC.visibility_of_element_located(self.AUTH))

    def sing_in(self):
        self.wait.until(EC.(self.AUTH))