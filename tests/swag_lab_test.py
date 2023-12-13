from PageObjects.swag.login_page import LoginPage
from Utilities.Common_ops import *


@pytest.mark.parametrize("username", get_csv("Username", "username"))
def test_swag_lab01(driver, username):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login_action(username, get_data("swagTest/password"))
