#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
#from utils.constants import LOGIN_PAGE_URL, recover_password_button, email_input, password_input, eye_button, input_status_active_attribute


class RecoverPasswordPage(BasePage):
    def check_transition_to_password_recovery_page(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert expected_result == actual_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'
