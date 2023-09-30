from pages.base_page import BasePage
from components.components import WebElement


class Droppable(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.draggable = WebElement(driver, '#draggable')
        self.droppable = WebElement(driver, '#droppable')
