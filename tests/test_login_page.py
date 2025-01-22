import pytest
from pages.login_page import LogInPage
import time
from tests.conftest import setup


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login(self):
        log_in_page = LogInPage(self)
        time.sleep(1)
        log_in_page.open()
        time.sleep(1)
        log_in_page.basic_auth()
        time.sleep(3)
        log_in_page.submit_alert()
        log_in_page.validate_credentials()
        # log_in_page.set_user_inputs("user@phptravels.com", "demouser")
        # welcome_msg = "Hi, Demo User"
        # assert welcome_msg in self.driver.find_element(
        #     *UserAccountLocators.welcome_msg).text
        # log_in_page.expand_account_menu()
        # log_in_page.logout()
