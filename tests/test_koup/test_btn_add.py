from conftest import browser
from pages.herokuapp import HerokuApp
from pages.herokuapp_add_remove import HerokuAddRemove
import time


def test_koup(browser):
    hk_page = HerokuApp(browser)
    hkar_page = HerokuAddRemove(browser)

    hk_page.visit()
    assert hk_page.add_remove.get_text() == 'Add/Remove Elements'
    hk_page.add_remove.click()
    time.sleep(2)
    assert hkar_page.equal_url()
    assert hkar_page.btn_add.get_text() == 'Add Element'
    assert hkar_page.btn_add.get_dom_attribute('onclick') == "addElement()"

    for i in range(4):
        hkar_page.btn_add.click()

    for el in hkar_page.btns_del.find_elements():
        assert str(el.text) == 'Delete'

