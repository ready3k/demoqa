from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.user_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.usr_name_output = WebElement(driver, 'p.mb-1:nth-child(1)')
        self.current_addr_output = WebElement(driver, 'p.mb-1:nth-child(2)')
