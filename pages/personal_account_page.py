from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):
    @allure.step('Проверка перехода в Личный кабинет')
    def check_transition_to_personal_account(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert actual_result == expected_result

    @allure.step('Проверка перехода в Историю заказов')
    def check_transition_to_orders_history(self, element, expected_result):
        orders_history_link = self.driver.find_element(*element)
        actual_result = orders_history_link.get_attribute('class')
        
        assert expected_result in actual_result 

    @allure.step('Проверка выхода из Личного кабинета')
    def check_logout(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert actual_result == expected_result
