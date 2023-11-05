import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/BasePage.log").get_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def navigate(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.error(f"Element not found within {timeout} seconds: {locator}")
            raise

    def set(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def get_title(self):
        return self.driver.title

    def get_page_source(self):
        return self.driver.page_source