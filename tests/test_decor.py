import pytest

from conftest import browser
from pages.demoqa import DemoQA
from pages.radio_button import RadioButton


@pytest.mark.skip
def test_decor(browser):
    demoqa_page = DemoQA(browser)

    demoqa_page.visit()
    assert demoqa_page.h5_text.check_count_elements(6)
    for el in demoqa_page.h5_text.find_elements():
        assert not el.text == ""


# @pytest.mark.skipif(True, reason="Just Skip")
def test_radio(browser):
    rb_page = RadioButton(browser)

    if not rb_page.code_status() == 200:
        pytest.skip(reason=f"Страница {rb_page.base_url} недоступна")

    rb_page.visit()
    assert 'disable' in rb_page.no_radio_btn.get_dom_attribute('class')
    rb_page.yes_btn.click_force()
    assert rb_page.text_field.get_text() == 'Yes'
    rb_page.impressive_btn.click_force()
    assert rb_page.text_field.get_text() == 'Impressive'
