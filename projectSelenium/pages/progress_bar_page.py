from base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProgressBarLocators


class ProgressBar(BasePage):  # Page of progres bar
    def work_with_progress_bar(self, name_attribute, stop_value):
        self.click_method(*ProgressBarLocators.BUTTON_START)  # Find element(button start) and click it
        progress_status = WebDriverWait(self.browser, 30, 0.001).until(
            EC.text_to_be_present_in_element_attribute(ProgressBarLocators.PROGRESS_BAR, name_attribute,
                                                       stop_value))  # Wait while value of progress bar get stop_value then return true
        if progress_status:  # When value of progress bar get stop value click button stop
            value_progress_bar = self.get_attribute_method(*ProgressBarLocators.PROGRESS_BAR, name_attribute)
            print(f" Value of progress bar is: {value_progress_bar}")
            self.click_method(*ProgressBarLocators.BUTTON_STOP)
        value_result = self.receive_text_method(
            *ProgressBarLocators.RESULT)  # Find element (result) and receive text of sentence of stopping progress bar
        value_duration = int(value_result[(value_result.rfind(' ') + 1)::])  # Receive value of duration from text on the button
        print(f" Value of duration is: {value_duration}")
        return value_duration
