from pages.main_page import MainPage
from pages.text_input_page import TextInput
import pytest


@pytest.mark.parametrize('execution_number', range(3))  # Execute test 3 times
def test_input_random_text(browser, execution_number):  # Test checking whether input sentence is equal output one
    link = "http://uitestingplayground.com/"
    mp = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
    mp.open()  # Open main page
    mp.go_to_text_input_page()  # Execute method page, go to log in page
    url = mp.get_current_url()  # Get current URL
    value_input = mp.generate_random_string(5)  # Generate a random sentence to input it in the field
    ti = TextInput(browser, url)  # Execute method page, go to log in page
    values_button = ti.input_random_text(value_input)  # Execute method page, receive a changed name of button
    mp.assertion_values_text(value_input, values_button)  # Compare the input sentence and the sentence on the button




