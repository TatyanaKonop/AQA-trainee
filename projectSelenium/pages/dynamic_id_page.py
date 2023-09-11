from base.base_page import BasePage
from pages.locators import DynamicIDPageLocators
import time


class DynamicID(BasePage):  # Page with button dynamic ID
    def click_dynamic_button(self):
        dynamic_button = self.browser.find_element(*DynamicIDPageLocators.BUTTON_WITH_DYNAMIC_ID)
        dynamic_button.click()


