import time
from conftest import browser
from pages.alerts import Alerts


def test_alerts(browser):
    a_page = Alerts(browser)

    a_page.visit()
    assert not a_page.alert()
    a_page.alert_btn.click()
    time.sleep(2)
    assert a_page.alert()
    a_page.alert().accept()


def test_alert_text(browser):
    a_page = Alerts(browser)

    a_page.visit()
    a_page.alert_btn.click()
    time.sleep(2)
    assert a_page.alert().text == "You clicked a button"
    a_page.alert().accept()
    assert not a_page.alert()


def test_confirm(browser):
    a_page = Alerts(browser)

    a_page.visit()
    a_page.conf_btn.click()
    time.sleep(2)
    a_page.alert().dismiss()
    assert a_page.conf_res.get_text() == 'You selected Cancel'


def test_prompt(browser):
    a_page = Alerts(browser)

    a_page.visit()
    a_page.promt_btn.click_force()
    time.sleep(2)
    a_page.alert().send_keys('Roma')
    a_page.alert().accept()
    assert a_page.prompt_res.get_text() == 'You entered Roma'
    time.sleep(2)


def test_timer_alert(browser):
    a_page = Alerts(browser)

    a_page.visit()
    assert not a_page.alert()
    a_page.timer_alert_button.click_force()
    time.sleep(3)
    assert not a_page.alert()
    time.sleep(2)
    assert a_page.alert()
    a_page.alert().accept()
    assert not a_page.alert()
