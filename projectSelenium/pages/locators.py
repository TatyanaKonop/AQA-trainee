from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_DYNAMIC_BUTTON = (By.LINK_TEXT, "Dynamic ID")
    LINK_TEXT_INPUT = (By.LINK_TEXT, "Text Input")
    LINK_PROGRESS_BAR = (By.LINK_TEXT, "Progress Bar")
    LINK_SAMPLE_APP = (By.LINK_TEXT, "Sample App")


class DynamicIDPageLocators:
    BUTTON_WITH_DYNAMIC_ID = (By.CSS_SELECTOR, '.btn.btn-primary')


class TextInputLocators:
    INPUT_FIELD = (By.XPATH, '//input[@class="form-control"]')
    BUTTON_WITH_CHANGED_TEXT = (By.XPATH, '//button[@class="btn btn-primary"]')


class ProgressBarLocators:
    BUTTON_START = (By.XPATH, '//button[@class="btn btn-primary btn-test"]')
    BUTTON_STOP = (By.XPATH, '//button[@class="btn btn-info btn-test"]')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar bg-info"]')
    RESULT = (By.XPATH, '//p[@id="result"]')


class SampleAppLocators:
    INPUT_LOGIN = (By.XPATH, '//input[@name="UserName"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="Password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@class="btn btn-primary"]')
    LABEL_LOGIN = (By.XPATH, '//label[@id="loginstatus"]')
