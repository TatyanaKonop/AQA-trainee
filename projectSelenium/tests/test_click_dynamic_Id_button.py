from pages.main_page import MainPage
from pages.dynamic_id_page import DynamicID


def test_click_dynamic_id_button(browser, send_link):
    instance_main_page = MainPage(browser,
                                  send_link)  # initialize the Page Object, pass the driver instance and url to the constructor
    instance_main_page.open()  # Open main page
    instance_main_page.go_to_dynamic_id_page()  # Execute method page, go to page with dynamic Id button
    url = instance_main_page.get_current_url()  # Get current URL

    instance_dynamic_id_page = DynamicID(browser, url)  # Execute transition between pages
    instance_dynamic_id_page.click_dynamic_button()  # Click button  not using locator iD
