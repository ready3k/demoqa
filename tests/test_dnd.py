import time

from conftest import browser
from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_dd(browser):
    dd_page = Droppable(browser)
    action_chains = ActionChains(browser)

    dd_page.visit()

    assert dd_page.droppable.check_css('background-color', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        dd_page.draggable.find_element(),
        dd_page.droppable.find_element()
    ).perform()
    assert dd_page.droppable.check_css('background-color', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(
        dd_page.draggable.find_element(),
        -200, -50
        ).perform()
    assert dd_page.droppable.check_css('background-color', 'rgba(70, 130, 180, 1)')
    time.sleep(1)
