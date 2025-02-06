import json


class ConfigReader:
    CONFIG_PATH = "configs/config.json"
    BASE_URL = "https://the-internet.herokuapp.com/"
    SUPPORTED_BROWSERS = ["chrome", "firefox"]

    def __init__(self, config_path=CONFIG_PATH):
        self.config_path = config_path
        self.config_data = self._load_config()

    def _load_config(self):
        with open(self.config_path, "r") as file:
            return json.load(file)

    def get_value(self, key):
        return self.config_data.get(key)

    def get_supported_browsers(self):
        return self.SUPPORTED_BROWSERS
