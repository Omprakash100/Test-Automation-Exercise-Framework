from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/signup.log").get_logger()

class SignupPage(BasePage):
    NAME_FIELD = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = ConfigReader.get_signup_url()
        logger.info("SignupPage initialized with URL: %s", self.url)

    def navigate_to_signup_page(self):
        logger.info("Navigating to signup page: %s", self.url)
        self.navigate(self.url)

    def enter_name(self, name):
        logger.info("Entering name: %s", name)
        self.set(self.NAME_FIELD, name)
        return self

    def enter_email(self, email):
        logger.info("Entering email: %s", email)
        self.set(self.EMAIL_FIELD, email)
        return self

    def click_signup(self):
        logger.info("Clicking signup button")
        self.click(self.SIGNUP_BUTTON)