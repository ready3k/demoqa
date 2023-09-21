from conftest import browser
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    testelements_page = ElementsPage(browser)

    testelements_page.visit()
    assert testelements_page.test_loc.check_count_elements(9)
