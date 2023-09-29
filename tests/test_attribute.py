from conftest import browser
from pages.text_box import TextBox


def test_placeholder(browser):
    tb_page = TextBox(browser)

    tb_page.visit()
    assert tb_page.user_name.get_dom_attribute('placeholder') == 'Full Name'
