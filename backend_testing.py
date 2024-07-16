import requests
import pymysql
from db_secrets import DB_HOST, DB_PORT, DB_USER, DB_SCHEMA, DB_PASSWORD

user_id = 999
requests.post(f'http://127.0.0.1:5600/users/{user_id}', json={'user_name': 'Agatha'})
get_user_data = requests.get(f'http://127.0.0.1:5600/users/{user_id}')


def check_user_in_db():
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE ID='{user_id}'")
    user_db = cursor.fetchall()
    if user_db[0][0] == user_id:
        print('Database user record registered successfully')


def check_web_app():
    if get_user_data.status_code == 200 and get_user_data.json()['user_name'] == 'Agatha':
        print('Web app working!')


check_user_in_db()
check_web_app()
