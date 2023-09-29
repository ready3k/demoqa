from conftest import browser
from pages.elements_page import ElementsPage


def test_flex_menu(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.block_menu.check_css('flex', '0 0 25%')
    assert el_page.block_menu.check_css('max-width', '25%')
    browser.set_window_size(320, 480)
    assert el_page.block_menu.check_css('flex', '0 0 100%')
    assert el_page.block_menu.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)
