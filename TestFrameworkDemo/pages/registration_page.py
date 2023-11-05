from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/registration.log").get_logger()

class RegistrationPage(BasePage):
    TITLE_MR = (By.ID, "uniform-id_gender1")
    TITLE_MRS = (By.ID, "uniform-id_gender2")
    PASSWORD_FIELD = (By.ID, "password")
    FIRST_NAME_FIELD = (By.ID, "first_name")
    LAST_NAME_FIELD = (By.ID, "last_name")
    COMPANY_FIELD = (By.ID, "company")
    ADDRESS1_FIELD = (By.ID, "address1")
    STATE_FIELD = (By.ID, "state")
    CITY_FIELD = (By.ID, "city")
    ZIPCODE_FIELD = (By.ID, "zipcode")
    MOBILE_NUMBER_FIELD = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    def __init__(self, driver):
        super().__init__(driver)
        logger.info("RegistrationPage initialized")

    def select_title(self, title):
        logger.info("Selecting title: %s", title)
        if title == "Mr.":
            self.click(self.TITLE_MR)
        else:
            self.click(self.TITLE_MRS)
        return self

    def enter_password(self, password):
        logger.info("Entering password")
        self.set(self.PASSWORD_FIELD, password)
        return self

    def enter_first_name(self, first_name):
        logger.info("Entering first name: %s", first_name)
        self.set(self.FIRST_NAME_FIELD, first_name)
        return self

    def enter_last_name(self, last_name):
        logger.info("Entering last name: %s", last_name)
        self.set(self.LAST_NAME_FIELD, last_name)
        return self

    def enter_company(self, company):
        logger.info("Entering company: %s", company)
        self.set(self.COMPANY_FIELD, company)
        return self

    def enter_address(self, address):
        logger.info("Entering address: %s", address)
        self.set(self.ADDRESS1_FIELD, address)
        return self

    def enter_state(self, state):
        logger.info("Entering state: %s", state)
        self.set(self.STATE_FIELD, state)
        return self

    def enter_city(self, city):
        logger.info("Entering city: %s", city)
        self.set(self.CITY_FIELD, city)
        return self

    def enter_zipcode(self, zipcode):
        logger.info("Entering zipcode: %s", zipcode)
        self.set(self.ZIPCODE_FIELD, zipcode)
        return self

    def enter_mobile_number(self, number):
        logger.info("Entering mobile number: %s", number)
        self.set(self.MOBILE_NUMBER_FIELD, number)
        return self

    def click_create_account_button(self):
        logger.info("Clicking create account button")
        self.click(self.CREATE_ACCOUNT_BUTTON)
        return HomePage(self.driver)

