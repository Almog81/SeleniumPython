import allure
from allure_commons.types import AttachmentType


def verifai_txt(expected, result):
    try:
        assert expected == result
    except AssertionError:
        screenshot("Expected: " + expected + " Result is: " + result)
        assert False


def screenshot(name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)