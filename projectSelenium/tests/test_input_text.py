from pages.main_page import MainPage
from pages.text_input_page import TextInput
import pytest

@pytest.mark.parametrize('execution_number',  range(3))  # Execute test 3 times
def test_input_random_text(browser, execution_number, send_link, generate_random_string):  # Test checking whether input sentence is equal output one
    instance_main_page = MainPage(browser, send_link)  # initialize the Page Object, pass the driver instance and url to the constructor
    instance_main_page.open()  # Open main page
    instance_main_page.go_to_text_input_page()  # Execute method page, go to log in page
    url = instance_main_page.get_current_url()  # Get current URL
    instance_text_input_page = TextInput(browser, url)  # Execute method page, go to log in page
    value_input = generate_random_string
    values_button = instance_text_input_page.input_random_text(value_input)  # Execute method page, receive a changed name of button
    assert value_input == values_button, 'Text is diffent'  # Compare the input sentence and the sentence on the button




