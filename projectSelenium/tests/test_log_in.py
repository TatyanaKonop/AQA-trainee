from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_log_in_successful(browser, send_link, login_and_password):  # Positive test log in
    login_password = login_and_password[0]
    login = login_password["login"]
    password = login_password["password"]
    message_successful = ' '.join(login_and_password[2])
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



def test_log_in_failed(browser, send_link, login_and_password):  # Negative test log in
    login_password = login_and_password[1]
    login = login_password["login"]
    password = login_password["password"]
    message_warning = ' '.join(login_and_password[3])
    instance_main_page = MainPage(browser,
                                  send_link)  # initialize the Page Object, pass the driver instance and url to the constructor
    instance_main_page.open()  # Open main page
    instance_main_page.go_log_in_page()  # Execute method page, go to log in page
    url = instance_main_page.get_current_url()  # Get current URL

    instance_log_in_page = LoginPage(browser, url)  # Execute transition between pages
    result = instance_log_in_page.log_in(login, password)  # Execute method page, receive message
    # Checking content of greeting message after successful log in
    assert message_warning == result, "Log in isn't failed, there is no a warning message"
