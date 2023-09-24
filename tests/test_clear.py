from conftest import browser
from pages.text_box import TextBox
import time


def test_clear(browser):
    tb_page = TextBox(browser)

    tb_page.visit()
    tb_page.user_name.send_keys('This message is self-destroyed after 3..2..1..')
    time.sleep(2)
    tb_page.user_name.clear()
    time.sleep(2)
    assert tb_page.user_name.get_text() == ''
