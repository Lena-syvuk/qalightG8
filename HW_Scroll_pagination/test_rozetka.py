from HW_Scroll_pagination.page_rozetka import PageRozetkaNotebooks


class TestRozetkaScrolling:

    def test_scroll_and_click_load_more(self, chrome):
        expected_goods_cnt = 180
        page = PageRozetkaNotebooks(chrome)
        page.open()
        page.is_scroll_and_click_load_more()
        amount = page.get_goods_count()
        assert amount == expected_goods_cnt

    def test_scroll_and_chsoose_page_7(self,chrome):
        page = PageRozetkaNotebooks(chrome)
        page.open()
        page.is_scroll_and_choose_page_7()
        assert page.validation_of_page()








