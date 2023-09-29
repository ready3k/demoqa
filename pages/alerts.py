from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.alert_btn = WebElement(driver, '#alertButton')
        self.conf_btn = WebElement(driver, '#confirmButton')
        self.conf_res = WebElement(driver, '#confirmResult')
        self.promt_btn = WebElement(driver, '#promtButton')
        self.prompt_res = WebElement(driver, '#promptResult')
        self.timer_alert_button = WebElement(driver, '#timerAlertButton')
