import configparser

class ConfigReader:
    config = configparser.ConfigParser()
    config.read(r"config.properties")

    @staticmethod
    def get_base_url():
        return ConfigReader.config.get('URLS', 'BASE_URL')

    @staticmethod
    def get_login_url():
        login_url = ConfigReader.get_base_url() + ConfigReader.config.get('URLS', 'LOGIN_URL')
        return login_url

    @staticmethod
    def get_signup_url():
        signup_url = ConfigReader.get_base_url() + ConfigReader.config.get('URLS', 'SIGNUP_URL')
        return signup_url

    @staticmethod
    def get_adblocker_path():
        return ConfigReader.config.get('FilePath', 'ADBLOCKER')

    @staticmethod
    def get_login_data_file_path():
        return ConfigReader.config.get('FilePath', 'LOGIN_DATA')

    @staticmethod
    def get_registration_data():
        registration_data = {
            'name': ConfigReader.config.get('RegistrationData', 'SAMPLE_NAME'),
            'email': ConfigReader.config.get('RegistrationData', 'SAMPLE_EMAIL'),
            'title': ConfigReader.config.get('RegistrationData', 'TITLE_MR'),
            'password': ConfigReader.config.get('RegistrationData', 'SAMPLE_PASSWORD'),
            'first_name': ConfigReader.config.get('RegistrationData', 'SAMPLE_FIRST_NAME'),
            'last_name': ConfigReader.config.get('RegistrationData', 'SAMPLE_LAST_NAME'),
            'company': ConfigReader.config.get('RegistrationData', 'SAMPLE_COMPANY'),
            'address': ConfigReader.config.get('RegistrationData', 'SAMPLE_ADDRESS'),
            'state': ConfigReader.config.get('RegistrationData', 'SAMPLE_STATE'),
            'city': ConfigReader.config.get('RegistrationData', 'SAMPLE_CITY'),
            'zipcode': ConfigReader.config.get('RegistrationData', 'SAMPLE_ZIPCODE'),
            'mobile_number': ConfigReader.config.get('RegistrationData', 'SAMPLE_MOBILE_NUMBER')
        }
        return registration_data