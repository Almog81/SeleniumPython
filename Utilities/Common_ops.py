import csv
import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from xml.etree.ElementTree import ParseError, parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Utilities.verifications import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


wait = None
action = None


def get_data(tag_name):
    try:
        # Parse the XML file
        tree = parse("Configuration/DataConfig.xml")
        root = tree.getroot()

        # Find the element with the specified tag name
        element = root.find(tag_name)

        # Check if the element is found
        if element is not None:
            return element.text
        else:
            print(f"Tag '{tag_name}' not found in the XML file.")
            return None

    except ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None


def get_csv(file_name, tag_mame):
    with open("DDTFiles/" + file_name + ".csv", 'r') as file:
        reader = csv.DictReader(file)
        return [row[tag_mame] for row in reader]


def get_json(file_name, tag_name):
    with open("DDTFiles/" + file_name + ".json", 'r') as file:
        data = json.load(file)
        usernames = data[tag_name]
        return {tag_name: usernames}


def start_test(platform):
    if platform == 'web':
        return start_browser_test(get_data("BrowserName"))
    elif platform == 'mobile':
        return start_mobile_test()
    elif platform == 'api':
        return start_api_test()
    elif platform == 'electron':
        return start_electron_test()
    elif platform == 'desktop':
        return start_desktop_test()
    else:
        print(f"Unsupported platform: {platform}")
        return None


def start_mobile_test():
    # Implement your mobile test setup here
    pass


def start_api_test():
    # Implement your API test setup here
    pass


def start_electron_test():
    # Implement your Electron test setup here
    pass


def start_desktop_test():
    # Implement your desktop test setup here
    pass


def start_browser_test(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "chromium":
        return webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    elif browser_name == "brave":
        return webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    elif browser_name == "edge":
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        service.log_path = "firefox.log"
        service.log_level = "info"
        return webdriver.Firefox(service=service)
    elif browser_name == "IE":
        return webdriver.Ie(service=IEService(IEDriverManager().install()))
    else:
        print("Can't find Browser type")
        return None


@pytest.fixture(autouse=True, scope='session')
def driver():
    global wait, action
    platform = get_data("Platform")
    driver = start_test(platform)
    wait = WebDriverWait(driver, 15)
    action = ActionChains(driver)
    if driver:
        driver.maximize_window()
        driver.implicitly_wait(10)
        # Yield the driver
        yield driver
        # Return from The yield
        time.sleep(2)
        driver.close()
        driver.quit()
        print("Test Completed!")


def screenshot(name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)


if __name__ == "__main__":
    pytest.main()
