from pages.personal_account_page import PersonalAccountPage
import allure
from utils.constants import (
    BASE_URL, email_input, password_input, personal_account_link, orders_history_link, 
    enter_button, link_status_active_attribute, exit_button
    )


class TestPersonalAccountPage:
    @allure.title('Переход в «Личный кабинет»')
    @allure.description('Открытие главной страницы, логин юзера и переход в личный кабинет по клику')
    def test_transition_to_login_page(self, driver, test_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(BASE_URL)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.enter_data(email_input, test_user['email'])
        personal_account_page.click_element(password_input)
        personal_account_page.enter_data(password_input, test_user['password'])
        personal_account_page.click_element(enter_button)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.check_transition_to_personal_account(orders_history_link, 'История заказов')

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Открытие главной страницы, логин юзера, переход в личный кабинет и в раздел с заказами по клику')
    def test_transition_to_orders_history_page(self, driver, test_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(BASE_URL)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.enter_data(email_input, test_user['email'])
        personal_account_page.click_element(password_input)
        personal_account_page.enter_data(password_input, test_user['password'])
        personal_account_page.click_element(enter_button)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.click_element(orders_history_link)
        personal_account_page.check_transition_to_orders_history(orders_history_link, link_status_active_attribute)

    @allure.title('Выход из аккаунта')
    @allure.description('Открытие главной страницы, логин юзера и выход из аккаунта по клику')
    def test_logout(self, driver, test_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.open_page(BASE_URL)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.enter_data(email_input, test_user['email'])
        personal_account_page.click_element(password_input)
        personal_account_page.enter_data(password_input, test_user['password'])
        personal_account_page.click_element(enter_button)
        personal_account_page.wait_for_clickable(personal_account_link)
        personal_account_page.click_element(personal_account_link)
        personal_account_page.click_element(exit_button)
        personal_account_page.check_logout(enter_button, 'Войти')

