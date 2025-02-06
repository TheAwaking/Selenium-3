from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    def __init__(self, driver):
        self.driver = driver

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()
