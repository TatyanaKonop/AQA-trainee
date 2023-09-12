import pytest
from selenium import webdriver
import random
import string

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


@pytest.fixture(scope="function")  # login and password, successful and warning messages data
def login_and_password():
    correct_dict_login_password = {"login": "Rert", "password": "pwd"}
    incorrect_dict_login_password = {"login": "Rert", "password": "Pwd"}
    message_successful = tuple(map(str, f'Welcome, {correct_dict_login_password["login"]}!'.split()))
    message_when_log_in_failed = tuple(map(str, 'Invalid username/password'.split()))
    return correct_dict_login_password, incorrect_dict_login_password, message_successful, message_when_log_in_failed

@pytest.fixture(scope="function")
def generate_random_string(length=5):  # Method for generation sentence used in the test_input_text
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        print(type(rand_string))
        return rand_string

