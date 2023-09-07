from HW_RadioButton.page_radio_button import PageRadioButton

class TestRadioButtons:
    current_button_info ={
        'Yes': {},
        'Impressive': {},
        'No':{}
    }

    def test_print_dict(self, chrome):
        page = PageRadioButton(driver=chrome)
        page.open()
        self.current_button_info['Yes']['is_enabled'] = page.is_yes_button_enable()
        self.current_button_info['Yes']['is_selected'] = page.is_yes_button_selected()
        self.current_button_info['Impressive']['is_enabled'] = page.is_impressive_button_enable()
        self.current_button_info['Impressive']['is_selected'] = page.is_impressive_button_selected()
        self.current_button_info['No']['is_enabled'] = page.is_no_button_enable()
        self.current_button_info['No']['is_selected'] = page.is_no_button_selected()
        print(self.current_button_info)
