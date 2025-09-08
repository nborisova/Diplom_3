from pages.orders_feed import OrdersFeedPage
import allure
from utils.api_client import create_order
from utils.constants import (
    LOGIN_PAGE_URL, ORDER_FEED_PAGE_URL, email_input, password_input, enter_button, order_feed_link, order_feed_title, 
    build_burger_title, order_card, composition_title, all_order_cards, completed_for_all_time_counter, completed_today_counter
    )


class TestOrdersFeedPage:
    @allure.title('Открытие попапа с деталями заказа')
    @allure.description('Открытие попапа с детялями заказа при клике на него')
    def test_check_open_order_popup(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(ORDER_FEED_PAGE_URL)
        orders_feed_page.wait_for_clickable(order_card)
        orders_feed_page.click_element(order_card)
        orders_feed_page.check_title(composition_title, 'Cостав')

    @allure.title('Заказ пользователя из раздела «История заказов» отображается в «Лента заказов»')
    @allure.description('Логин юзером, создание заказа, сравнение номера созданного заказа с номерами в общей ленте')
    def test_user_order_is_display_in_feed(self, driver, test_user):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(LOGIN_PAGE_URL)
        orders_feed_page.wait_for_clickable(email_input)
        orders_feed_page.enter_data(email_input, test_user['email'])
        orders_feed_page.click_element(password_input)
        orders_feed_page.enter_data(password_input, test_user['password'])
        orders_feed_page.click_element(enter_button)
        orders_feed_page.wait_for_load_element(build_burger_title)
        orders_feed_page.click_element(order_feed_link)
        orders_feed_page.wait_for_load_element(order_feed_title)
        expected_order = f"#0{test_user['user_order_number']}"
        orders_feed_page.check_user_order_in_feed(all_order_cards, expected_order)

    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании нового заказа')
    @allure.description('Создание юзера и заказа, сравнение значений счетчика до и после заказа')
    def test_completed_counter_increases_after_new_order(self, driver, test_user):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(ORDER_FEED_PAGE_URL)
        old_value = orders_feed_page.get_counter(completed_for_all_time_counter)

        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        create_order(test_user['token'], ingredients)

        orders_feed_page.driver.refresh()
        orders_feed_page.wait_for_load_element(completed_for_all_time_counter)
        orders_feed_page.check_counter_increase(completed_for_all_time_counter, old_value)

    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании нового заказа')
    @allure.description('Создание юзера и заказа, сравнение значений счетчика до и после заказа')
    def test_completed_counter_today_increases_after_new_order(self, driver, test_user):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(ORDER_FEED_PAGE_URL)
        old_value = orders_feed_page.get_counter(completed_today_counter)

        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        create_order(test_user['token'], ingredients)
        
        orders_feed_page.driver.refresh()
        orders_feed_page.wait_for_load_element(completed_today_counter)
        orders_feed_page.check_counter_increase(completed_today_counter, old_value)

    @allure.title('Отображение номера заказа в разделе "В работе" после его оформления')
    @allure.description('Создание юзера и заказа, сравнение значений в поле')
    def test_order_number_in_progress(self, driver, test_user):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(ORDER_FEED_PAGE_URL)

        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        create_order(test_user['token'], ingredients)

        expected_order = f"0{test_user['user_order_number']}"
        orders_feed_page.check_order_in_progress(expected_order)