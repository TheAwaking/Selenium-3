import pytest
from pages.login_page import LogInPage
import time
from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open()
        log_in_page.basic_auth()
        log_in_page.cred_alert()
        result_text = log_in_page.validate_credentials()
        expected_alert_text = "Basic Auth\nCongratulations! You must have the proper credentials."

        assert expected_alert_text == result_text, f"Expected alert text: '{expected_alert_text}', but got: '{result_text}'"
