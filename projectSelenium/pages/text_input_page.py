from base.base_page import BasePage
from pages.locators import TextInputLocators


class TextInput(BasePage):
    def input_random_text(self, value_input):
        print(f'Input random text: {value_input}')
        self.send_keys_method(*TextInputLocators.INPUT_FIELD,
                              value_input)  # Receive element (input field) and send text
        self.click_method(*TextInputLocators.BUTTON_WITH_CHANGED_TEXT)  # Receive element (button) and click
        values_button = self.receive_text_method(
            *TextInputLocators.BUTTON_WITH_CHANGED_TEXT)  # Receive element (button) and text on it
        print(f'Output random text: {values_button}')
        return values_button
