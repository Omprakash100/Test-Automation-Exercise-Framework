from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/home.log").get_logger()

class HomePage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = ConfigReader.get_base_url()
        logger.info("HomePage initialized")

    def navigate_to_home_page(self):
        logger.info("Navigating to home_page: %s", self.url)
        self.navigate(self.url)

    def click_logout(self):
        logger.info("Clicking logout button")
        self.click(self.LOGOUT_BUTTON)