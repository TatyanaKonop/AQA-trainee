from pages.main_page import MainPage
from pages.login_page import LoginPage
from .conftest import LogIn


def test_log_in_successful(browser, send_link):  # Positive test log in
    login = LogIn.CORRECT_LOGIN_PASSWORD["login"]
    password = LogIn.CORRECT_LOGIN_PASSWORD["password"]
    message_successful = ' '.join(LogIn.MESSAGE_SUCCESSFUL)
    instance_main_page = MainPage(browser,
                                  send_link)  # initialize the Page Object, pass the driver instance and url
    # to the constructor
    instance_main_page.open()  # Open main page
    instance_main_page.go_log_in_page()  # Execute method page, go to log in page
    url = instance_main_page.get_current_url()  # Get current URL

    instance_log_in_page = LoginPage(browser, url)  # Execute transition between pages
    result = instance_log_in_page.log_in(login, password)  # Execute method page, receive message
    # Checking content of greeting message after successful log in
    assert message_successful == result, "Log in isn't successful, there is no a greeting message"


def test_log_in_failed(browser, send_link):  # Negative test log in
    login = LogIn.INCORRECT_LOGIN_PASSWORD["login"]
    password = LogIn.INCORRECT_LOGIN_PASSWORD["password"]
    message_warning = ' '.join(LogIn.MESSAGE_WHEN_LOG_IN_FAILED)
    instance_main_page = MainPage(browser,
                                  send_link)  # initialize the Page Object, pass the driver instance and url to the constructor
    instance_main_page.open()  # Open main page
    instance_main_page.go_log_in_page()  # Execute method page, go to log in page
    url = instance_main_page.get_current_url()  # Get current URL

    instance_log_in_page = LoginPage(browser, url)  # Execute transition between pages
    result = instance_log_in_page.log_in(login, password)  # Execute method page, receive message
    # Checking content of warning message after successful log in
    assert message_warning == result, "Log in isn't failed, there is no a warning message"
