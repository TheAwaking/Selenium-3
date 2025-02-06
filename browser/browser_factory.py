from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from enum import StrEnum
from selenium.webdriver.support.wait import WebDriverWait


class BrowserName(StrEnum):
    CHROME = "chrome"
    FIREFOX = "firefox"


class DriverFactory:

    @staticmethod
    def get_driver(config):
        if config["browser"] == BrowserName.CHROME:
            options = webdriver.ChromeOptions()
            if config["browser_options"]["start_maximized"]:
                options.add_argument("start-maximized")
            if config["browser_options"]["headless"]:
                options.add_argument("--headless")
            elif config["browser"] == BrowserName.FIREFOX:
                options = webdriver.FirefoxOptions()

            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            return driver
        available_browsers = [name.value for name in BrowserName]
        raise ValueError(f"Provide valid browser name. Available browsers: {', '.join(available_browsers)}")
