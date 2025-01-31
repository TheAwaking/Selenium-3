import json
import pytest
from browser.browser_factory import DriverFactory
from base_elements.base_element import BaseElement
from pages.login_page import LogInPage

CONFIG_PATH = "../configs/config.json"
SUPPORTED_BROWSERS = ["chrome"]
DEFAULT_URL = "https://the-internet.herokuapp.com/"


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope='session')
def browser_setup(config):
    if "browser" not in config:
        raise ValueError('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise ValueError(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def url_setup(config):
    return config["hero_url"] if "hero_url" in config else DEFAULT_URL


@pytest.fixture(scope='function')
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    browser = BaseElement(driver)
    request.cls.driver = driver
    request.cls.browser = browser
    yield
    browser.quit()
