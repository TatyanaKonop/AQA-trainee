from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_log_in_failed(browser):  # Negative test log in with wrong password
    link = "http://uitestingplayground.com/"
    login = "Yes"
    password = 'pwD'
    sample_warning_message = 'Invalid username/password'
    mp = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
    mp.open()  # Open main page
    mp.go_log_in_page()  # Execute method page, go to log in page
    url = mp.get_current_url()  # Get current URL

    lp = LoginPage(browser, url)  # Execute transition between pages
    result = lp.log_in(login, password)  # Execute method page

    mp.assertion_values_text(sample_warning_message, result)  # Checking content of warning message after failed log in
    print("Log in is failed")
