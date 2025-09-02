import pytest
from selenium import webdriver


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
