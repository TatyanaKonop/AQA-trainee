from pages.main_page import MainPage
from pages.dynamic_id_page import DynamicID



def test_click_dynamic_id_button(browser):
    LINK = "http://uitestingplayground.com/"
    mp = MainPage(browser, LINK)  # initialize the Page Object, pass the driver instance and url to the constructor
    mp.open()  # Open main page
    mp.go_to_dynamic_id_page()  # Execute method page, go to page with dynamic Id button
    url = mp.get_current_url()  # Get current URL

    dp = DynamicID(browser, url)  # Execute transition between pages
    dp.click_dynamic_button()  # Click button  not using locator iD



