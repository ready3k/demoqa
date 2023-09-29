from conftest import browser
from pages.web_tables import WebTables
from selenium.webdriver.common.keys import Keys


def test_wtables(browser):
    wt_page = WebTables(browser)

    wt_page.visit()
    assert not wt_page.text_flag.get_text() == ''
    assert not wt_page.no_rows_found.exist()

    while wt_page.delete_btns.exist():
        wt_page.delete_btns.click()

    assert wt_page.no_rows_found.exist()


def test_np_bttns(browser):
    wt_page = WebTables(browser)

    type_list = ['Firstname', 'LastName', 'user@email.com', 23, 100, 'department']

    wt_page.visit()
    wt_page.rows_per_page.scroll_to_element()
    wt_page.rows_per_page.click()
    wt_page.rows_per_page.send_keys(Keys.UP)
    wt_page.rows_per_page.send_keys(Keys.RETURN)
    wt_page.add_btn.scroll_to_element()
    assert wt_page.next_button.get_dom_attribute('disabled')
    assert wt_page.prev_button.get_dom_attribute('disabled')
    counter = 0
    while wt_page.pages_count.get_text() == '1':
        counter += 1
        wt_page.add_btn.click()
        wt_page.mod_first_name.send_keys(type_list[0])
        wt_page.mod_last_name.send_keys(type_list[1])
        wt_page.mod_user_email.send_keys(type_list[2])
        wt_page.mod_age.send_keys(type_list[3])
        wt_page.mod_salary.send_keys(type_list[4])
        wt_page.mod_department.send_keys(type_list[5])
        wt_page.mod_submit_btn.click()
    assert counter == 3
    assert wt_page.pages_count.get_text() == '2'
    assert not wt_page.next_button.get_dom_attribute('disabled')
    assert wt_page.page_jump.get_dom_attribute('value') == "1"
    wt_page.next_button.click_force()
    assert wt_page.page_jump.get_dom_attribute('value') == "2"
    wt_page.prev_button.click_force()
    assert wt_page.page_jump.get_dom_attribute('value') == "1"
