from base.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_dynamic_id_page(self):  # Go to page with dynamic ID button
        self.click_method(*MainPageLocators.LINK_DYNAMIC_BUTTON)

    def go_to_text_input_page(self):  # Go to page with field for changing name button
        self.click_method(*MainPageLocators.LINK_TEXT_INPUT)

    def go_progress_bar_page(self):  # Go to page with progress bar
        self.click_method(*MainPageLocators.LINK_PROGRESS_BAR)

    def go_log_in_page(self):  # Go to log in page
        self.click_method(*MainPageLocators.LINK_SAMPLE_APP)
