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

    def click_method(self, how, what):
        element = self.browser.find_element(how, what)
        element.click()

    def send_keys_method(self, how, what, value_input):
        element = self.browser.find_element(how, what)
        element.send_keys(value_input)

    def receive_text_method(self, how, what):  # Get text of element
        element = self.browser.find_element(how, what)
        element = element.text
        return element

    def get_attribute_method(self, how, what, name_attribute):
        element = self.browser.find_element(how, what)
        value_attribute = element.get_attribute(name_attribute)
        return value_attribute
