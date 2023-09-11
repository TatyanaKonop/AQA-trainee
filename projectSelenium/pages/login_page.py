from base.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import SampleAppLocators


class LoginPage(BasePage):  # Log in page
    def log_in(self, login, password):
        input_login = self.browser.find_element(*SampleAppLocators.INPUT_LOGIN)
        input_login.send_keys(login)  # Input login
        input_password = self.browser.find_element(*SampleAppLocators.INPUT_PASSWORD)
        input_password.send_keys(password)  # Input password
        button_login = self.browser.find_element(*SampleAppLocators.BUTTON_LOGIN)
        button_login.click()  # Click button login
        label_login = self.browser.find_element(*SampleAppLocators.LABEL_LOGIN)
        value_label_login = label_login.text  # Receive text of message
        return value_label_login

