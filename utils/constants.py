from selenium.webdriver.common.by import By


BASE_URL = 'https://stellarburgers.nomoreparties.site'
LOGIN_PAGE_URL = f'{BASE_URL}/login'
RECOVER_PASSWORD_PAGE_URL = f'{BASE_URL}/forgot-password'
RESET_PASSWORD_PAGE_URL = f'{BASE_URL}/reset-password'
ORDER_FEED_PAGE_URL = f'{BASE_URL}/feed'
GET_AND_CREATE_ORDERS_URL = f'{BASE_URL}/api/orders'

recover_password_link = (By.XPATH, './/a[text()="Восстановить пароль"]')
email_input = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
password_input = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')
eye_button = (By.CSS_SELECTOR, 'div.input__icon.input__icon-action')
recover_password_button = (By.XPATH, './/button[contains(text(),"Восстановить")]')
password_field = (By.XPATH, './/div[label[text()="Пароль"]]')

input_status_active_attribute = 'input_status_active'
link_status_active_attribute = 'Account_link_active__2opc9'

personal_account_link = (By.XPATH, './/p[contains(text(),"Личный Кабинет")]')
orders_history_link = (By.XPATH, './/a[contains(text(),"История заказов")]')
enter_button = (By.XPATH, './/button[contains(text(),"Войти")]')
exit_button = (By.XPATH, './/button[contains(text(),"Выход")]')

constructor_link = (By.XPATH, './/p[contains(text(),"Конструктор")]')
order_feed_link = (By.XPATH, './/p[contains(text(),"Лента Заказов")]')
build_burger_title = (By.XPATH, './/h1[contains(text(),"Соберите бургер")]')
order_feed_title = (By.XPATH, './/h1[contains(text(),"Лента заказов")]')

ingredient = (By.XPATH, './/ul[contains(@class, "BurgerIngredients_ingredients__list__2A-mT")]/a[1]')
ingredient_detail_title = (By.XPATH, './/h2[contains(text(),"Детали ингредиента")]')
close_popup_button = (By.XPATH, './/button[contains(@class, "Modal_modal__close_modified__3V5XS")]') 
ingredient_basket = (By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]') 
ingredient_counter = (By.XPATH, './/ul[contains(@class, "BurgerIngredients_ingredients__list__2A-mT")]/a[1]//p[contains(@class, "counter_counter__num__3nue1")]')
create_order_button = (By.XPATH, './/button[contains(text(),"Оформить заказ")]')
order_id = (By.XPATH, './/p[contains(text(),"идентификатор заказа")]')

order_card = (By.XPATH, './/li[contains(@class, "OrderHistory_listItem__2x95r")][1]')
composition_title = (By.XPATH, './/p[contains(text(),"Cостав")]')
all_order_cards = (By.CSS_SELECTOR, ".OrderFeed_list__OLh59")  
completed_for_all_time_counter = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
completed_today_counter = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
