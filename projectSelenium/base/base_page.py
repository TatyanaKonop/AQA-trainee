import random
import string


class BasePage:
    # Initialization base class
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):  # Open app
        self.browser.get(self.url)

    def get_current_url(self):  # Get current URL
        current_url = self.browser.current_url
        print(f'Current URL {current_url}')

    @staticmethod
    def assertion_values_text(sample, result):  # Method for assertion
        assert sample == result
        print(f'Assertion is true')

    @staticmethod
    def generate_random_string(length):  # Method for generation sentence
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
