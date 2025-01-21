import pytest
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open()
        log_in_page.open_basic_auth()
        log_in_page.sing_in()
        log_in_page.validate_credentials()
        log_in_page.set_user_inputs("user@phptravels.com", "demouser")
        welcome_msg = "Hi, Demo User"
        assert welcome_msg in self.driver.find_element(
            *UserAccountLocators.welcome_msg).text
        log_in_page.expand_account_menu()
        log_in_page.logout()
