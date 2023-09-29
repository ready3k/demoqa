import time

from conftest import browser
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    bt_page = BrowserTab(browser)

    bt_page.visit()
    assert len(browser.window_handles) == 1
    bt_page.new_tab.click_force()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
