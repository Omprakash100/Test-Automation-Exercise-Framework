import pytest
from pages.registration_page import RegistrationPage
from utils.config_reader import ConfigReader
from utils.logger import CustomLogger
from utils import utility

logger = CustomLogger(__name__, "log/registration.log").get_logger()

@pytest.fixture(scope="class")
def registration_page(driver):
    driver_manager = driver
    registration_page = RegistrationPage(driver_manager)
    yield registration_page

@pytest.mark.order(2)
class TestRegistration:
    @pytest.mark.parametrize("registration_data", [ConfigReader.get_registration_data()])
    def test_registration(self, registration_page, registration_data):
        logger.info("Starting registration test...")

        registration_page.select_title(registration_data.get("title")) \
            .enter_password(registration_data.get("password")) \
            .enter_first_name(registration_data.get("first_name")) \
            .enter_last_name(registration_data.get("last_name")) \
            .enter_company(registration_data.get("company")) \
            .enter_address(registration_data.get("address")) \
            .enter_state(registration_data.get("state")) \
            .enter_city(registration_data.get("city")) \
            .enter_zipcode(registration_data.get("zipcode")) \
            .enter_mobile_number(registration_data.get("mobile_number"))

        home_page = registration_page.click_create_account_button()

        page_source = registration_page.get_page_source()
        assert 'Account Created!' in page_source

        utility.write_csv_data(ConfigReader.get_login_data_file_path(), [registration_data.get("email"), registration_data.get("password")])
        logger.info("Registration test completed.")

        home_page.navigate_to_home_page()
        home_page.click_logout()
        logger.info("Successful logout after successful Registration.")
