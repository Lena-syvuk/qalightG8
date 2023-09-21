
from selenium.webdriver.common.by import By
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageDynamicProperties:

    URL = 'https://demoqa.com/dynamic-properties'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.enable_after_button_loc = (By.XPATH,'//button[@id="enableAfter"]')
        self.visible_after_button_loc = (By.CSS_SELECTOR, '#visibleAfter')
        self.change_color_loc = (By.XPATH,'//button[@id="colorChange"]')

    def open(self):
        self.driver.get(self.URL)

    def get_enable_after_button_element(self):
        element = self.driver.find_element(*self.enable_after_button_loc)
        return element

    def button_change_color(self):
        return self.change_color_loc

    def get_visible_after_button_element(self, element):
        return element


def wait_until_element_is_enabled(element:WebElement, max_wait_time = 10,polling_time = 0.1) -> bool:
    end_time = time.monotonic() + max_wait_time
    while time.monotonic() < end_time:
        if element.is_enabled():
            break
        else:
            time.sleep(polling_time)
            continue
    return element.is_enabled()


def wait_until_element_is_displayed(driver: WebDriver, locator: tuple, max_wait_time = 10, polling_time = 0.1):
    element = None
    end_time = time.monotonic() + max_wait_time
    while time.monotonic() < end_time:
        try:
            element = driver.find_element(*locator)
            break
        except NoSuchElementException:
            time.sleep(polling_time)
            continue
    return element




