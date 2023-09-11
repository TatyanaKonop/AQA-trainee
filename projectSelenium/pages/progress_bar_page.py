from base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProgressBarLocators


class ProgressBar(BasePage): # Page of progres bar
    def work_with_progress_bar(self):
        button_start = self.browser.find_element(*ProgressBarLocators.BUTTON_START)
        button_start.click()
        progress_status = WebDriverWait(self.browser, 30, 0.001).until(
            EC.text_to_be_present_in_element_attribute(ProgressBarLocators.PROGRESS_BAR, 'aria-valuenow', '50'))
        if progress_status:
            progress_bar = self.browser.find_element(*ProgressBarLocators.PROGRESS_BAR)
            value_progress_bar = progress_bar.get_attribute('aria-valuenow')
            print(f" Value of progress bar is: {value_progress_bar}")
            button_stop = self.browser.find_element(*ProgressBarLocators.BUTTON_STOP)
            button_stop.click()
        result = self.browser.find_element(*ProgressBarLocators.RESULT)
        value_result = result.text  # Receive value of sentence of stopping progress bar
        value_duration = int(value_result[(value_result.rfind(' ') + 1)::])  # Receive value of duration
        print(f" Value of duration is: {value_duration}")
        return value_duration
