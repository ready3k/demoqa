from conftest import browser
from pages.elements_page import ElementsPage
from pages.checkbox import CheckBox


def test_find_elements(browser):
    testelements_page = ElementsPage(browser)

    testelements_page.visit()
    assert testelements_page.test_loc.check_count_elements(9)


def test_count_checkbox(browser):
    cb_page = CheckBox(browser)

    cb_page.visit()
    assert cb_page.list_all.check_count_elements(1)
    cb_page.plus_btn.click()
    assert cb_page.list_all.check_count_elements(17)
    browser.refresh()
    assert cb_page.list_all.check_count_elements(1)
