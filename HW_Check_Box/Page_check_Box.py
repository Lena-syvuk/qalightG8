from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckBox:
    URL = 'https://demoqa.com/checkbox'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.expand_collapse_button = '//span[text()="{}"]//ancestor::span/button/*[contains(@class, "icon-expand")]'
        self.check_uncheck_label = '//label[@for="tree-node-{}"]'


    def open(self):
        self.driver.get(self.URL)

    def expand_node_by_name(self, name):
        trigger = 'close'
        self.expand_or_collapse_node(name=name, trigger=trigger)

    def collapse_node_by_name(self, name):
        trigger = 'open'
        self.expand_or_collapse_node(name=name, trigger=trigger)

    def expand_or_collapse_node(self, name, trigger):
        xpath = self.expand_collapse_button.format(name)
        element = self.driver.find_element(By.XPATH, xpath)
        if trigger in element.get_attribute('class'):
            element.click()

    def expand_nodes_from_list(self, nodes: list):
        for node in nodes:
            self.expand_node_by_name(node)

    def select_check_boxes_from_list(self, boxes: list):
        for box in boxes:
            self.check_folder(box)

    def check_folder(self, name: str):
        check_uncheck_input = f'{self.check_uncheck_label.format(name.lower())}/input'
        check_uncheck_label = f'{check_uncheck_input}/..'
        _input = self.driver.find_element(By.XPATH, check_uncheck_input)
        _label = self.driver.find_element(By.XPATH, check_uncheck_label)
        if not _input.is_selected():
            _label.click()

    def results_check_box(self):
        locator = '//div[@id="result"]//span[@class="text-success"]'
        selected_elements = self.driver.find_elements(By.XPATH, locator)
        return [element.text for element in selected_elements]













