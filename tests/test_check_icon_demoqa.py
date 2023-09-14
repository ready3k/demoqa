from conftest import browser
from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    assert demo_page.exist_icon()
    demo_page.click_on_the_icon()
    assert demo_page.equal_url()


#     browser.get("https://demoqa.com/")
#     icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
#
#     if icon is None:
#         print('-')
#     else:
#         print('+')
