from conftest import browser
from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA


def test_navigation(browser):
    elements_page = ElementsPage(browser)
    demoqa_page = DemoQA(browser)

    demoqa_page.visit()
    demoqa_page.btn_elements.click()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()
