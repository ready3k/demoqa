from conftest import browser
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQA


def test_modal_elements(browser):
    md_page = ModalDialogs(browser)

    md_page.visit()
    assert md_page.sub_menu_btns.check_count_elements(5)


def test_navigation_modal(browser):
    md_page = ModalDialogs(browser)
    demoqa_page = DemoQA(browser)

    md_page.visit()
    browser.refresh()
    md_page.demoqa_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert demoqa_page.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)
