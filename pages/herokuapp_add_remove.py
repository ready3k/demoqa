from pages.base_page import BasePage
from components.components import WebElement


class HerokuAddRemove(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)
        self.btn_add = WebElement(driver, '/html/body/div[2]/div/div/button', 'xpath')
        self.btns_del = WebElement(driver, '#elements > button.added-manually')
