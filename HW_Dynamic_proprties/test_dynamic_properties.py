from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait

from HW_Dynamic_proprties.page_dynamic_properties import PageDynamicProperties
from HW_Dynamic_proprties.page_dynamic_properties import wait_until_element_is_enabled, wait_until_element_is_displayed


class TestDynamicProperties:

    def test_1(self,chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        element = page.get_enable_after_button_element()
        wait_until_element_is_enabled(element)
        is_element_enabled = element.is_enabled()
        assert is_element_enabled

    def test_2(self,chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        button = page.button_change_color()
        changed_color_button = WebDriverWait(chrome, 10)
        changed_color_button.until(es.text_to_be_present_in_element_attribute(button, "class","mt-4 text-danger btn btn-primary"))
        assert changed_color_button

    def test_3(self, chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        locator = page.visible_after_button_loc
        element = wait_until_element_is_displayed(chrome, locator)
        assert element.is_enabled()




