from pages.base_page import BasePage
from selenium.webdriver import ActionChains
import allure


class MainPage(BasePage):
    @allure.step('Сравнение текстового значения одного элемента с другим')
    def check_title(self, element, expected_result):
        self.wait_for_load_element(element)
        actual_result = self.driver.find_element(*element).text

        assert actual_result == expected_result

    @allure.step('Перетаскивание элемента в другую область')
    def drag_and_drop_element(self, source_element, target_element):
        source = self.driver.find_element(*source_element)  
        target = self.driver.find_element(*target_element)  
        ActionChains(self.driver).drag_and_drop(source, target).perform()