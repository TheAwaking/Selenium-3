import json

from selenium.webdriver.support.ui import WebDriverWait


class PageBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        with open('../config.json') as config_file:
            config = json.load(config_file)
            self.hero_url = config["hero_url"]

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def cred_alert(self):
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth/")
