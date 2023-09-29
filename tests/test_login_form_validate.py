from conftest import browser
from pages.form_page import FormPage
from pages.web_tables import WebTables


def test_placeholder(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert not form_page.user_email.get_dom_attribute('pattern') == ''
    form_page.btn_submit.click_force()
    assert not form_page.modal_dialog.exist()
    assert form_page.user_form.get_dom_attribute('class') == "was-validated"


def test_webtables_form(browser):
    wt_page = WebTables(browser)
    type_list = ['Firstname', 'LastName', 'user@email.com', 23, 100, 'department']

    wt_page.visit()
    assert wt_page.add_btn.exist()
    assert not wt_page.reg_form_modal.exist()
    wt_page.add_btn.click()
    assert wt_page.reg_form_modal.exist()
    wt_page.mod_submit_btn.click()
    assert wt_page.reg_form_modal.exist()
    wt_page.mod_first_name.send_keys(type_list[0])
    wt_page.mod_last_name.send_keys(type_list[1])
    wt_page.mod_user_email.send_keys(type_list[2])
    wt_page.mod_age.send_keys(type_list[3])
    wt_page.mod_salary.send_keys(type_list[4])
    wt_page.mod_department.send_keys(type_list[5])
    wt_page.mod_submit_btn.click()
    assert not wt_page.reg_form_modal.exist()
    wt_page.table_edit_btn.click()
    assert wt_page.reg_form_modal.exist()
    wt_page.mod_first_name.clear()
    type_list[0] = 'NewName'
    wt_page.mod_first_name.send_keys(type_list[0])
    wt_page.mod_submit_btn.click()
    wt_page.table_delete_btn.click()
