from PageObjects.google.main_page import MainPage
from Utilities.Common_ops import *


def test_swag_lab01(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.search_action()
    print(get_data("googleTest/google"))