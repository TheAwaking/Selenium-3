from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, driver, name):
        self.wait = None
        self.driver = driver
        self.name = None

    def wait_for_open(self):
        self.wait.until(EC.presence_of_element_located(By.XPATH, self.UNIQUE_ELEMENT_LOC))
