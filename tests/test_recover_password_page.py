from pages.recover_password_page import RecoverPasswordPage
import allure
from utils.constants import (
    LOGIN_PAGE_URL, RECOVER_PASSWORD_PAGE_URL, RESET_PASSWORD_PAGE_URL, recover_password_link, 
    email_input, password_input, eye_button, password_field, input_status_active_attribute, recover_password_button)


class TestRecoverPasswordPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Открытие страницы логина и клик на кнопку «Восстановить пароль»')
    def test_transition_to_password_recovery_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(LOGIN_PAGE_URL)
        recover_password_page.wait_for_clickable(recover_password_link)
        recover_password_page.click_element(recover_password_link)
        recover_password_page.check_transition_to_password_recovery_page(email_input, '')

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_on_recover_button(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(RECOVER_PASSWORD_PAGE_URL)
        recover_password_page.wait_for_clickable(email_input)
        recover_password_page.enter_data(email_input, 'test@test.com')
        recover_password_page.click_element(recover_password_button)
        recover_password_page.check_transition_to_reset_password_page(RESET_PASSWORD_PAGE_URL)
        recover_password_page.check_enter_email_and_click_on_recover_button(password_input, '')
    
    @allure.title('Активация подсветки поля пароля при клике на иконку глаза')
    @allure.description('Открытие страницы восставновления пароля, ввод пароля и клик на иконку глаза')
    def test_check_active_password_field(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(RECOVER_PASSWORD_PAGE_URL)
        recover_password_page.wait_for_clickable(email_input)
        recover_password_page.enter_data(email_input, 'test@test.com')
        recover_password_page.click_element(recover_password_button)
        recover_password_page.check_transition_to_reset_password_page(RESET_PASSWORD_PAGE_URL)
        recover_password_page.enter_data(password_input, 'qazedc!1')
        recover_password_page.click_element(eye_button)
        recover_password_page.check_border_for_field_is_active(password_field, input_status_active_attribute)

