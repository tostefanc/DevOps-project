import requests
import pymysql
from db_secrets import DB_HOST, DB_PORT, DB_USER, DB_SCHEMA, DB_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_id = 0
user_name = 'Agatha'
requests.post(f'http://127.0.0.1:5600/users/{user_id}', json={'user_name': f'{user_name}'})
get_user_data = requests.get(f'http://127.0.0.1:5600/users/{user_id}')


def check_user_in_db():
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE ID='{user_id}'")
    user_db = cursor.fetchall()
    if user_db[0][0] == user_id:
        print('Database user record registered successfully')
    else:
        raise Exception("database record test failed")


def check_web_app():
    if get_user_data.status_code == 200 and get_user_data.json()['user_name'] == f'{user_name}':
        print('Web app working!')
    else:
        raise Exception("web app test failed")


def frontend_testing():
    driver = webdriver.Chrome(service=Service(""))
    driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
    user_element = driver.find_element(By.ID, value='user')
    if user_element:
        print(user_element.text)
    else:
        raise Exception("frontend test failed")


check_user_in_db()
check_web_app()
frontend_testing()
