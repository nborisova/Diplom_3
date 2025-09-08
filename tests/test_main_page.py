from pages.main_page import MainPage
import allure
from utils.constants import (
    BASE_URL, LOGIN_PAGE_URL, email_input, password_input, enter_button, order_feed_link, 
    order_feed_title, build_burger_title, constructor_link, ingredient, ingredient_detail_title, 
    close_popup_button, ingredient_basket, ingredient_counter, create_order_button, order_id
    )


class TestMainPage:
    @allure.title('Переходы на страницы «Конструктор» и «Лента заказов»')
    @allure.description('Переход на страницы по кликам')
    def test_transition_to_constructor_and_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.wait_for_load_element(order_feed_link)
        main_page.click_element(order_feed_link)
        main_page.wait_for_load_element(order_feed_title)
        main_page.check_title(order_feed_title, 'Лента заказов')

        main_page.click_element(constructor_link)
        main_page.wait_for_load_element(build_burger_title)
        main_page.check_title(build_burger_title, 'Соберите бургер')

    @allure.title('Открытие и закрытие попапа с деталями ингридиента')
    @allure.description('Открытие попапа и его закрытие по кликом на крестик')
    def test_check_popup_is_opened_closed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.wait_for_load_element(build_burger_title)
        main_page.click_element(ingredient)
        main_page.wait_for_load_element(ingredient_detail_title)
        main_page.check_title(ingredient_detail_title, 'Детали ингредиента')

        main_page.wait_for_clickable(close_popup_button)
        main_page.click_element(close_popup_button)
        main_page.wait_for_load_element(build_burger_title)
        main_page.check_title(build_burger_title, 'Соберите бургер')

    @allure.title('Увеличение каунтера ингредиента при добавлении в заказ')
    @allure.description('Клик на ингредиент и его перетаскивание в область заказа')
    def test_ingredient_counter_is_changed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.wait_for_load_element(build_burger_title)
        main_page.drag_and_drop_element(ingredient, ingredient_basket)
        main_page.check_title(ingredient_counter, '2')

    @allure.title('Создание заказа залогиненным юзером')
    @allure.description('Логин юзером и оформление заказа')
    def test_create_order_by_authorized_user(self, driver, test_user):
        main_page = MainPage(driver)
        main_page.open_page(LOGIN_PAGE_URL)
        main_page.wait_for_clickable(email_input)
        main_page.enter_data(email_input, test_user['email'])
        main_page.click_element(password_input)
        main_page.enter_data(password_input, test_user['password'])
        main_page.click_element(enter_button)
        main_page.wait_for_load_element(build_burger_title)
        main_page.drag_and_drop_element(ingredient, ingredient_basket)
        main_page.click_element(create_order_button)
        main_page.wait_for_load_element(order_id)
        main_page.check_title(order_id, 'идентификатор заказа')


