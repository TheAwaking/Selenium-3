import json
import pytest
from browser.browser_factory import DriverFactory

CONFIG_PATH = "../config.json"
DEFAULT_WAIT_TIME = 20
SUPPORTED_BROWSERS = ["chrome"]
DEFAULT_URL = "https://the-internet.herokuapp.com/"


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    request.cls.driver = driver
    yield
    driver.quit()
