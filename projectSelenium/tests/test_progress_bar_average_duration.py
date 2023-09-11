from pages.main_page import MainPage
from pages.progress_bar_page import ProgressBar
import pytest
import statistics



def test_progress_bar(browser):
    sum = 0
    n = 3  # Number of repetition of test
    for i in range(n):
        link = "http://uitestingplayground.com/"
        mp = MainPage(browser, link)  # initialize the Page Object, pass the driver instance and url to the constructor
        mp.open()  # Open main page
        mp.go_progress_bar_page()  # Execute method page, go to log in page
        url = mp.get_current_url()  # Get current URL

        pb = ProgressBar(browser, url)  # Execute method page, go to log in page
        value_duration = pb.work_with_progress_bar()  # Execute method page, receive duration
        sum = sum + value_duration  # Sum of duration
    average = sum / n  # Average of duration
    print(f'Average duration is: {average}')




