from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure


class OrdersFeedPage(BasePage):
    @allure.step('Сравнение текстового значения одного элемента с другим')
    def check_title(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert actual_result == expected_result

    @allure.step('Проверка наличия в ленте заказов заказа юзера')
    def check_user_order_in_feed(self, element, expected_result):
        feed_orders = self.driver.find_elements(*element)  
        feed_texts = [order.text for order in feed_orders]

        assert any(expected_result in text for text in feed_texts), \
            f"Заказ {expected_result} не найден в ленте заказов"

    @allure.step('Получение значения счетчика')
    def get_counter(self, counter_locator):
        counter_elem = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(counter_locator)
        )

        return int(counter_elem.text)

    @allure.step('Проверка увеличения значения счетчика')
    def check_counter_increase(self, completed_counter, old_value):
            new_value = int(self.driver.find_element(*completed_counter).text)
            assert new_value == old_value + 1

    @allure.step('Проверка отображения заказа юзера в поле "В работе:"')
    def check_order_in_progress(self, expected_result):
        
        WebDriverWait(self.driver, 5).until(
            lambda d: any(
                expected_result == li.text
                for li in d.find_elements(By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]/li')
            )
        )

        li_elements = self.driver.find_elements(By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__1YFem")]/li')
        actual_texts = [li.text for li in li_elements]
        assert expected_result in actual_texts