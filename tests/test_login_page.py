import pytest
from pages.login_page import LogInPage
from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login(self, url_setup):
        log_in_page = LogInPage(self.driver)
        login_url = f"{url_setup}/login"
        self.driver.get(login_url)
        log_in_page.click_auth_button()
        base_url = f"{url_setup}/basic_auth/"
        username = "admin"
        password = "admin"
        log_in_page.cred_alert(base_url, username, password)
        result_text = log_in_page.validate_credentials()
        expected_alert_text = "Basic Auth\nCongratulations! You must have the proper credentials."

        assert expected_alert_text == result_text, f"Expected alert text: '{expected_alert_text}', but got: '{result_text}'"
