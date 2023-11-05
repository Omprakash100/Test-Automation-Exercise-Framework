from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from utils.config_reader import ConfigReader
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/login.log").get_logger()

class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = ConfigReader.get_login_url()
        logger.info("LoginPage initialized with URL: %s", self.url)

    def navigate_to_login_page(self):
        logger.info("Navigating to login page: %s", self.url)
        self.navigate(self.url)

    def enter_email(self, email):
        logger.info("Entering email: %s", email)
        self.set(self.EMAIL_FIELD, email)
        return self

    def enter_password(self, password):
        logger.info("Entering password")
        self.set(self.PASSWORD_FIELD, password)
        return self

    def click_login(self):
        logger.info("Clicking login button")
        self.click(self.LOGIN_BUTTON)
        return HomePage(self.driver)