import requests
import random
import string
import allure
from utils.constants import BASE_URL, GET_AND_CREATE_ORDERS_URL


def generate_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase, k=6))}@test.com"

@allure.step('Создаем юзера')
def create_test_user(email, password, name):
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)
    response.raise_for_status()
    return payload

@allure.step('Авторизуем юзера')
def login_test_user(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post(f'{BASE_URL}/api/auth/login', json=payload)
    response.raise_for_status()
    return response.json()['accessToken']

@allure.step('Создаем заказ')
def create_order(user_token, ingredients):
    response = requests.post(GET_AND_CREATE_ORDERS_URL, json=ingredients, headers={'Authorization': user_token})
    response.raise_for_status()
    return response.json()['order']['number']

@allure.step('Удаляем юзера')
def delete_test_user(token):
    response = requests.delete(f'{BASE_URL}/api/auth/user', headers={'Authorization': token})
    response.raise_for_status()