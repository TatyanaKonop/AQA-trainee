from base.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import SampleAppLocators


class LoginPage(BasePage):  # Log in page
    def log_in(self, login, password):
        self.send_keys_method(*SampleAppLocators.INPUT_LOGIN, login)  # Input login
        self.send_keys_method(*SampleAppLocators.INPUT_PASSWORD, password) # Input password
        self.click_method(*SampleAppLocators.BUTTON_LOGIN) # Click button login
        label_login = self.receive_text_method(*SampleAppLocators.LABEL_LOGIN)  # Receive text of message
        return label_login

