import pytest
from pages.signup_page  import SignupPage
from utils.config_reader import ConfigReader
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/signup.log").get_logger()

@pytest.fixture(scope="class")
def signup_page(driver):
    driver_manager = driver
    signup_page = SignupPage(driver_manager)
    signup_page.navigate_to_signup_page()
    yield signup_page

@pytest.mark.order(1)
class TestSignup:
    registration_data = ConfigReader.get_registration_data()

    @pytest.mark.parametrize("name, email", [(registration_data.get("name"), registration_data.get("email"))])
    def test_successful_signup(self, signup_page, name, email):
        logger.info("Starting successful signup test...")
        signup_page.enter_name(name) \
                   .enter_email(email) \
                   .click_signup()
        actual_title = signup_page.get_title()
        assert actual_title == 'Automation Exercise - Signup'
        logger.info("Successful signup test completed.")