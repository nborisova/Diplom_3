from selenium import webdriver
from pages.recover_password_page import RecoverPasswordPage
import allure
from utils.constants import LOGIN_PAGE_URL, recover_password_link, email_input, password_input, eye_button, input_status_active_attribute


class TestRecoverPasswordPage:
    def test_transition_to_password_recovery_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(LOGIN_PAGE_URL)
        recover_password_page.wait_for_clickable(recover_password_link)
        recover_password_page.click_element(recover_password_link)
        recover_password_page.check_transition_to_password_recovery_page(email_input, "Email")