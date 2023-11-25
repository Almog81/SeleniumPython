from selenium.webdriver.common.by import By
from Utilities.Common_ops import *
from PageObjects.base_page import BasePage


class MainPage(BasePage):

    txt_username = (By.ID, "user-name")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(get_data("googleTest/Url"))

    def search_action(self):
        print('search done')