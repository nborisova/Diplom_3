from selenium.webdriver.common.by import By


BASE_URL = 'https://stellarburgers.nomoreparties.site'
LOGIN_PAGE_URL = f'{BASE_URL}/login'

recover_password_link = (By.XPATH, './/a[text()="Восстановить пароль"]')
email_input = (By.XPATH, './/label[text()="Email"]')
password_input = (By.XPATH, './/label[text()="Пароль"]')
eye_button = (By.XPATH, './/div[@class ="input__icon input__icon-action"]/svg')

input_status_active_attribute = 'input_status_active'

