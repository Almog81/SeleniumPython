from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Utilities.Common_ops import *
from PageObjects.base_page import BasePage


class MainPage(BasePage):

    txt_search = (By.ID, "APjFqb")
    btn_search = (By.NAME, "btnK")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(get_data("googleTest/Url"))

    def search_action(self, word):
        self.driver.find_element(*self.txt_search).send_keys(word + Keys.ENTER)