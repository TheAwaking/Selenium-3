import json
from utils.url_utils import add_basic_auth_to_url


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        with open('../configs/config.json') as config_file:
            config = json.load(config_file)
            self.hero_url = config["hero_url"]
            self.timeout = config["wait_time"]

    def cred_alert(self, base_url, username, password):
        auth_url = add_basic_auth_to_url(base_url, username, password)
        self.driver.get(auth_url)
