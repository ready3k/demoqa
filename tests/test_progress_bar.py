import time

from conftest import browser
from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    pb_page = ProgressBar(browser)

    pb_page.visit()
    time.sleep(2)
    pb_page.start_btn.click()
    while True:
        if int(pb_page.progress_bar.get_dom_attribute('aria-valuenow')) > 49:
            pb_page.start_btn.click_force()
            break
    assert pb_page.progress_bar.get_dom_attribute('aria-valuenow') == '51'
    time.sleep(2)
