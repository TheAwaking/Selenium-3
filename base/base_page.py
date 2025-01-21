from selenium.webdriver.support.ui import WebDriverWait


class PageBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/")
