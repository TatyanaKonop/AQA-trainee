from base.base_page import BasePage
from pages.locators import DynamicIDPageLocators
import time
from selenium.webdriver.common.by import By


class DynamicID(BasePage):  # Page with button dynamic ID
    def click_dynamic_button(self):
        self.click_method(*DynamicIDPageLocators.BUTTON_WITH_DYNAMIC_ID) # Find element and click it


