from conftest import browser
from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    assert demo_page.icon.exist()
    demo_page.icon.click()
    assert demo_page.equal_url()
