from base.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_dynamic_id_page(self):  # Go to page with dynamic ID button
        link_dynamic_id_page = self.browser.find_element(*MainPageLocators.LINK_DYNAMIC_BUTTON)
        link_dynamic_id_page.click()

    def go_to_text_input_page(self):  # Go to page with field for changing name button
        link_input_text = self.browser.find_element(*MainPageLocators.LINK_TEXT_INPUT)
        link_input_text.click()

    def go_progress_bar_page(self):  # Go to page with progress bar
        link_progress_bar = self.browser.find_element(*MainPageLocators.LINK_PROGRESS_BAR)
        link_progress_bar.click()

    def go_log_in_page(self):  # Go to log in page
        link_sample_app = self.browser.find_element(*MainPageLocators.LINK_SAMPLE_APP)
        link_sample_app.click()
