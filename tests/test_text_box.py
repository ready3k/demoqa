from conftest import browser
from pages.text_box import TextBox


def test_text_box(browser, full_name: str = 'Full Name', current_address: str = 'Current Address'):
    tb_page = TextBox(browser)

    tb_page.visit()
    tb_page.user_name.send_keys(full_name)
    tb_page.current_address.send_keys(current_address)
    tb_page.btn_submit.click_force()
    assert full_name in tb_page.usr_name_output.get_text()
    assert current_address in tb_page.current_addr_output.get_text()
