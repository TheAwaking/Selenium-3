from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators
from base.base_page import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
CRED = (By.XPATH, "//p[contains(text(), 'Congratulations!')]")



class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_basic_auth(self):
        self.wait.until(EC.visibility_of_element_located(self.AUTH))

    def sing_in(self):
        self.wait.until(EC.alert_is_present(self.AUTH))
        alert = driver.switch_to.alert
        alert("username").send_keys("admin")
        alert("password").send_keys("admin")
        alert.accept()

    def validate_credentials(self):
        self.wait.until(EC.visibility_of_element_located(self.CRED))