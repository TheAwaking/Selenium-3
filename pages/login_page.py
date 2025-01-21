from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from base.base_page import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class LogInPage(PageBase):
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.XPATH, "//p[contains(text(), 'Congratulations!')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_basic_auth(self):
        self.wait.until(EC.visibility_of_element_located(self.AUTH))  # переход на страницу алерта

    def sing_in(self, driver):
        alert = Alert(driver)

        alert.send_keys("admin")
        alert.send_keys("\t")
        alert.send_keys("admin")
        alert.accept()

    def validate_credentials(self):
        self.wait.until(EC.visibility_of_element_located(self.CRED))  # проверка, что текст появился
