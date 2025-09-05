import pytest
from selenium import webdriver
from utils.api_client import generate_email, create_test_user, login_test_user, create_order, delete_test_user


@pytest.fixture(params=('chrome', 'firefox'))
def driver(request):
    browser_name = request.param

    if browser_name == 'chrome':
        driver_instance = webdriver.Chrome() 
    elif browser_name == 'firefox':
        driver_instance = webdriver.Firefox()
    else: 
        raise ValueError(f'Unsupported browser: {browser_name}')
    
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

@pytest.fixture
def test_user():
    email = generate_email()
    password = 'Password123'
    name = 'Test Name'
    ingredients = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    create_test_user(email, password, name)
    token = login_test_user(email, password)
    user_order_number = create_order(token, ingredients)

    yield {'email': email, 'password': password, 'name': name, 'token': token, 'user_order_number': user_order_number}

    delete_test_user(token)
