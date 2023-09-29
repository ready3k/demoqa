from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.reg_form_modal = WebElement(driver, '#registration-form-modal')
        self.mod_submit_btn = WebElement(driver, '#submit')
        self.mod_first_name = WebElement(driver, '#firstName')
        self.mod_last_name = WebElement(driver, '#lastName')
        self.mod_user_email = WebElement(driver, '#userEmail')
        self.mod_age = WebElement(driver, '#age')
        self.mod_salary = WebElement(driver, '#salary')
        self.mod_department = WebElement(driver, '#department')
#
        self.table_edit_btn = WebElement(driver, '#edit-record-4 > svg:nth-child(1) > path:nth-child(1)')
        self.table_delete_btn = WebElement(driver, '#delete-record-4 > svg:nth-child(1) > path:nth-child(1)')
        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.delete_btns = WebElement(driver, '[title="Delete"]')
        self.text_flag = WebElement(driver, 'div.rt-tr-group:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.rows_per_page = WebElement(driver, '[aria-label="rows per page"]')
        self.rows_per_page_5 = WebElement(driver, '[aria-label="rows per page"] > [value="5"]')
        self.pages_count = WebElement(driver, '[class="-totalPages"]')
        self.prev_button = WebElement(driver, '.-previous > button:nth-child(1)')
        self.next_button = WebElement(driver, '.-next > button:nth-child(1)')
        self.page_jump = WebElement(driver, 'span > div [aria-label="jump to page"]')
