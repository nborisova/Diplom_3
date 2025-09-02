from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    #скролл до элемента
    def scroll_down(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)   

    #дождаться загрузки блока 
    def wait_for_load_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    #дождаться кликабельности элемента 
    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))     

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

        overlay = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element_located(overlay)
            )
        except TimeoutException:
            pass

        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    #заполнение полей данными
    def enter_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)