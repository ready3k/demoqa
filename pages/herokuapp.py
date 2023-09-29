from pages.base_page import BasePage
from components.components import WebElement


class HerokuApp(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)
        self.add_remove = WebElement(driver, '/html/body/div[2]/div/ul/li[2]/a', 'xpath')
