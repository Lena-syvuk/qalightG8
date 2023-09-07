from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageRadioButton:
    URL = 'https://demoqa.com/radio-button'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.yes_radio_button_xpath = '//label[@for="yesRadio"]//ancestor::div[contains(@class, "radio")]'
        self.impressive_radio_button_xpath = '//label[@for="impressiveRadio"]//ancestor::div[contains(@class, "radio")]'
        self.no_radio_button_xpath = '//label[@for="noRadio"]//ancestor::div[contains(@class, "radio")]'

    def open(self):
        self.driver.get(self.URL)


# method 'select'
    def select_yes_button(self):
        locator = self.yes_radio_button_xpath + '/label'
        self.driver.find_element(By.XPATH, locator).click()

    def select_impressive_button(self):
        locator = self.impressive_radio_button_xpath + '/label'
        self.driver.find_element(By.XPATH, locator).click()

    def select_no_button(self):
        locator = self.no_radio_button_xpath + '/label'
        self.driver.find_element(By.XPATH, locator).click()


# is selected

    def is_yes_button_selected(self) -> bool:
        locator = self.yes_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_selected()

    def is_impressive_button_selected(self) -> bool:
        locator = self.impressive_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_selected()

    def is_no_button_selected(self) -> bool:
        locator = self.no_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_selected()
# is_enabled
    def is_yes_button_enable(self) -> bool:
        locator = self.yes_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_enabled()

    def is_impressive_button_enable(self) -> bool:
        locator = self.impressive_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_enabled()

    def is_no_button_enable(self) -> bool:
        locator = self.no_radio_button_xpath + '/input'
        return self.driver.find_element(By.XPATH, locator).is_enabled()







