import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader

def add_extension_to_chrome(driver, extension_path):
    driver.install_addon(extension_path, temporary=True)

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_extension(ConfigReader.get_adblocker_path())
    driver_manager = webdriver.Chrome(options=options)
    yield driver_manager
    driver_manager.quit()

def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.funcargs['driver']
        allure.attach(driver.get_screenshot_as_png(), name=f'{node.name}.png',
                      attachment_type=AttachmentType.PNG)

