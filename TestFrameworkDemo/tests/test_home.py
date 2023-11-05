import pytest
from pages.home_page import HomePage
from utils.utility import read_csv_data
from utils.logger import CustomLogger

logger = CustomLogger(__name__, "log/home.log").get_logger()

@pytest.fixture(scope="class")
def home_page(driver):
    driver_manager = driver
    home_page = HomePage(driver_manager)
    home_page.navigate_to_home_page()
    yield home_page

class TestHome:
    pass