import pytest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.utility import read_csv_data
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/login.log").get_logger()

@pytest.fixture(scope="class")
def login_page(driver):
    driver_manager = driver
    login_page = LoginPage(driver_manager)
    login_page.navigate_to_login_page()
    yield login_page

@pytest.mark.order(3)
class TestLogin:
    @pytest.mark.parametrize("email, password", read_csv_data(ConfigReader.get_login_data_file_path()))
    def test_successful_login(self, login_page, email, password):
        logger.info("Starting successful login test...")
        home_page = login_page.enter_email(email) \
                  .enter_password(password) \
                  .click_login()
        actual_title = login_page.get_title()
        assert actual_title == 'Automation Exercise'
        logger.info("Successful login test completed.")
        home_page.click_logout()
        logger.info("Successful logout after successful login.")