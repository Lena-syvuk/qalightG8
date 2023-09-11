import pytest
from HW_Check_Box.Page_check_Box import PageCheckBox
import time

class TestCheckBox:

    def test_1(self, chrome):

        directories = ['Home', 'Documents', 'Office']
        boxes = ['Public', 'Private']
        page = PageCheckBox(driver=chrome)
        page.open()
        page.expand_nodes_from_list(directories)
        page.select_check_boxes_from_list(boxes)
        results = page.results_check_box()
        print(results)







