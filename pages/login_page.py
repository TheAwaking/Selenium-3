from base.base_page import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LogInPage(PageBase):
    AUTH = (By.XPATH, "//a[contains(text(), 'Basic Auth')]")
    CRED = (By.XPATH, "//p[contains(text(), 'Congratulations!')]")

    def __init__(self, driver):
        super().__init__(driver)

    def basic_auth(self):
        self.wait.until(EC.visibility_of_element_located(self.AUTH)).click()

    def validate_credentials(self):
        self.wait.until(EC.visibility_of_element_located(self.CRED))
