import pytest
import time
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from conftest import browser
from pages.demoqa import DemoQA


def test_title(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_title() == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    assert page.get_title() == 'DEMOQA'
    assert page.for_robots.get_dom_attribute('name') == 'viewport'
    assert page.for_robots.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
