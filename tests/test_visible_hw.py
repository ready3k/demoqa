from conftest import browser
import time
from pages.accordian import Accordian


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert accordian_page.content_text_1.visible()
    accordian_page.content_text_1_header.click()
    time.sleep(2)
    assert not accordian_page.content_text_1.visible()


def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert not accordian_page.content_text_2_1.visible()
    assert not accordian_page.content_text_2_2.visible()
    assert not accordian_page.content_text_3.visible()
