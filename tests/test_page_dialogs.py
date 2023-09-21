from conftest import browser
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    md_page = ModalDialogs(browser)

    md_page.visit()
    assert md_page.sub_menu_btns.check_count_elements(5)
