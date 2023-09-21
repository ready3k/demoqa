from conftest import browser
from pages.demoqa import DemoQA


def test_title(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_title() == 'DEMOQA'

