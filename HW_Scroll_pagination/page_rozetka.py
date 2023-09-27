from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class PageRozetkaNotebooks:

    URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'




    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.goods_card_loc = (By.XPATH, '//li[contains(@class, "catalog-grid__cell")]')
        self.paginator_page = (By.XPATH, '//ul[starts-with(@class, "pagination")]//a[contains(@href, "notebooks/c80004/page=7/")]')
        self.load_more = (By.XPATH, '//a[@class="show-more show-more--horizontal"]')


    def open(self):
        self.driver.get(self.URL)



    def get_goods_count(self) -> int:
        elements = self.driver.find_elements(*self.goods_card_loc)
        return len(elements)

    def is_scroll_and_click_load_more(self):
        count = 3
        while count >1:
            element = self.driver.find_element(*self.load_more)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            count -= 1
            time.sleep(3)

    def is_scroll_and_choose_page_7(self):
        element = self.driver.find_element(*self.paginator_page)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(5)

    def validation_of_page(self):
        current_url = self.driver.current_url
        return current_url == 'https://rozetka.com.ua/ua/notebooks/c80004/page=7/'















