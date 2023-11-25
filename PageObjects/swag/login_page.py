from selenium.webdriver.common.by import By
from Utilities.Common_ops import *
from PageObjects.base_page import BasePage


class LoginPage(BasePage):

    txt_username = (By.ID, "user-name")
    txt_password = (By.NAME, "password")
    btn_login = (By.CLASS_NAME, "btn_action")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(get_data("swagTest/Url"))

    def login_action(self, username, password):
        self.driver.find_element(*self.txt_username).send_keys(username)
        self.driver.find_element(*self.txt_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()
