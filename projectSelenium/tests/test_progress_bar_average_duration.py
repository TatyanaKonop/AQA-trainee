from pages.main_page import MainPage
from pages.progress_bar_page import ProgressBar


def test_progress_bar(browser, name_attribute, stop_value, send_number_of_test_repetition, send_link):
    sum = 0

    for i in range(send_number_of_test_repetition):
        instance_main_page = MainPage(browser,
                                      send_link)  # initialize the Page Object, pass the driver instance and url to the constructor
        instance_main_page.open()  # Open main page
        instance_main_page.go_progress_bar_page()  # Execute method page, go to log in page
        url = instance_main_page.get_current_url()  # Get current URL
        instance_progress_bar_change = ProgressBar(browser, url)  # Execute method page, go to log in page
        value_duration = instance_progress_bar_change.work_with_progress_bar(name_attribute,
                                                                             stop_value)  # Execute method page, receive duration
        sum = sum + value_duration  # Sum of duration
    average = sum / send_number_of_test_repetition  # Average of duration
    print(f'Average duration is: {average}')
