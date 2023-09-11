from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_log_in_successful(browser):  # Positive test log in
    link = "http://uitestingplayground.com/"
    login = "Yes"
    password = 'pwd'
    sample_successful_message = f'Welcome, {login}!'
    mp = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
    mp.open()  # Open main page
    mp.go_log_in_page()  # Execute method page, go to log in page
    url = mp.get_current_url()  # Get current URL

    lp = LoginPage(browser, url) # Execute transition between pages
    result = lp.log_in(login, password) # Execute method page, receive message

    mp.assertion_values_text(sample_successful_message,
                             result)  # Cheking content of greeting message after successful log in
    print("Log in is succesful")
