from base.base_page import BasePage
from pages.locators import TextInputLocators


class TextInput(BasePage):
    def input_random_text(self, value_input):
        field_input = self.browser.find_element(*TextInputLocators.INPUT_FIELD)
        print(f'Input random text: {value_input}')
        field_input.send_keys(value_input)  # Input random sentence
        button_with_changed_text = self.browser.find_element(*TextInputLocators.BUTTON_WITH_CHANGED_TEXT)
        button_with_changed_text.click()  # Click button
        values_button = button_with_changed_text.text  # Receive text on the button
        print(f'Output random text: {values_button}')
        return values_button
