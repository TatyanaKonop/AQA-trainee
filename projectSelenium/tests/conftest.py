import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")  # Attribute for test_progress_bar_average_duration to get value of progress bar
def name_attribute():
    return 'aria-valuenow'


@pytest.fixture(scope="function")  # Value attribute for test_progress_bar_average_duration that is stop value
def stop_value():
    return '50'


@pytest.fixture(scope="function")  # Link data to create instance of browser
def send_link():
    return "http://uitestingplayground.com/"


@pytest.fixture(scope="function")  # Number of repetition of test
def send_number_of_test_repetition():
    return int(3)


@pytest.fixture(scope="function")  # Length of sentence for test test_input_text
def send_number_of_length():
    return int(5)


class LogIn:
    CORRECT_LOGIN_PASSWORD = {"login": "Rert", "password": "pwd"}
    INCORRECT_LOGIN_PASSWORD = {"login": "Rert", "password": "Pwd"}
    MESSAGE_SUCCESSFUL = tuple(map(str, f'Welcome, {CORRECT_LOGIN_PASSWORD["login"]}!'.split()))
    MESSAGE_WHEN_LOG_IN_FAILED = tuple(map(str, 'Invalid username/password'.split()))
