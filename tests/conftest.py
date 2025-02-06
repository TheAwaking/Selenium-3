import json
import pytest
from browser.browser import Browser
from browser.browser_factory import DriverFactory
from configs.ConfigReader import CONFIG_PATH, BASE_URL


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        return json.load(config_file)


@pytest.fixture(scope='session')
def url_setup(config):
    return config["hero_url"] if "hero_url" in config else BASE_URL


@pytest.fixture(scope='function')
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    browser = Browser(driver)
    request.cls.driver = driver
    request.cls.browser = browser
    yield
    browser.quit()
