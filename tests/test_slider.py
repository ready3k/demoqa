from conftest import browser
from pages.slider import Slider
from selenium.webdriver import Keys


def test_slider(browser):
    slider_page = Slider(browser)

    slider_page.visit()
    slider_page.slider.click()

    while slider_page.slider_value.get_dom_attribute('value') != '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_value.get_dom_attribute('value') == '50'
