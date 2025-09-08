from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure


class RecoverPasswordPage(BasePage):
    @allure.step('Проверка перехода на страницу восстановления пароля')
    def check_transition_to_password_recovery_page(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert expected_result == actual_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'

    @allure.step('Проверка перехода на страницу сброса пароля')
    def check_transition_to_reset_password_page(self, expected_url):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(expected_url)
        )
    @allure.step('Проверка ввода пароля и нажатия на кнопку восстановления пароля')
    def check_enter_email_and_click_on_recover_button(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).get_attribute('value')

        assert expected_result == actual_result, f'Ожидалось значение: "{expected_result}", получено "{actual_result}"'

    @allure.step('Проверка активации подсветки поля')
    def check_border_for_field_is_active(self, element, expected_result):
        password_field = self.driver.find_element(*element)
        actual_result = password_field.get_attribute('class')
        
        assert expected_result in actual_result 