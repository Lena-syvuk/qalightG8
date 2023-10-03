from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class PageRozetkaNotebooks:

    URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.goods_card_loc = (By.XPATH, '//li[contains(@class, "catalog-grid__cell")]')
        self.paginator_page_xpath = '//ul[starts-with(@class, "pagination")]//a[contains(@href, "page={}")]'
        self.load_more_loc = (By.XPATH, '//a[@class="show-more show-more--horizontal"]')

    def open(self):
        self.driver.get(self.URL)

    def choose_page(self, page_num):
        element = self.driver.find_element(By.XPATH,self.paginator_page_xpath.format(page_num))
        return element

    def get_goods_count(self) -> int:
        elements = self.driver.find_elements(*self.goods_card_loc)
        return len(elements)

    def scroll_and_click_load_more(self):
        count = 3
        while count >1:
            element = self.driver.find_element(*self.load_more_loc)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
            count -= 1
            time.sleep(3)

    def scroll_and_choose_page(self, page_num):
        element = self.choose_page(page_num)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(5)

    def is_page_number_correct(self, pag_num):
        current_url = self.driver.current_url
        return current_url == f'https://rozetka.com.ua/ua/notebooks/c80004/page={pag_num}/'















