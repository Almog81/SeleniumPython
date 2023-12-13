import csv
import json
import time

import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
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


@pytest.fixture()
def driver():
    driver = start_browser(get_data("BrowserName"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Yield the driver
    yield driver
    # Return from The yield
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test Completed!")


def start_browser(browser_name):
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
        print("Cant find Browser type")
