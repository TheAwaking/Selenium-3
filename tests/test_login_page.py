import pytest
from pages.login_page import LogInPage
from tests.conftest import setup
from configs.ConfigReader import ConfigReader
from utils.url_utils import add_basic_auth_to_url

LOGIN_PATH = "/login"
BASIC_AUTH_PATH = "/basic_auth/"
USERNAME = "admin"
PASSWORD = "admin"


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @pytest.mark.parametrize("url_setup")
    def test_login(self, url_setup):
        log_in_page = LogInPage(self.driver)
        login_url = f"{url_setup}{LOGIN_PATH}"
        self.driver.get(login_url)
        log_in_page.check_auth_page()
        log_in_page.click_auth_button()
        base_url = f"{url_setup}{BASIC_AUTH_PATH}"
        auth_url = add_basic_auth_to_url(base_url, USERNAME, PASSWORD)
        log_in_page.add_basic_auth_to_url(auth_url)
        result_text = log_in_page.validate_credentials()
        expected_alert_text = "Basic Auth\nCongratulations! You must have the proper credentials."

        assert expected_alert_text == result_text, f"Expected alert text: '{expected_alert_text}', but got: '{result_text}'"
