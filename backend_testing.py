import requests
import pymysql
from db_secrets import DB_HOST, DB_PORT, DB_USER, DB_SCHEMA, DB_PASSWORD

user_id = 999
requests.post(f'http://127.0.0.1:5600/users/{user_id}', json={'user_name': 'Agatha'})
get_user_data = requests.get(f'http://127.0.0.1:5600/users/{user_id}')


def check_user_in_db():
    """
     Verifies in the DB directly if the user has been created
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE ID='{user_id}'")
    user_db = cursor.fetchall()
    if user_db[0][0] == user_id:
        print('Database user record registered successfully')
    else:
        print('Test user does not exist')


def remove_test_user():
    """
    Removes the test user created by check_user_in_db function
    :return:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    cursor = db_connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE ID='{user_id}'")
    print('Removed the test user with ID: ', user_id)
    cursor.close()
    db_connection.close()


def check_web_app():
    """
    Checks web app module
    Tests if http response code is 200 and the received name is correct
    Prints "Web app working" if above checks are true
    """
    if get_user_data.status_code == 200 and get_user_data.json()['user_name'] == 'Agatha':
        print('Web app working!')


check_user_in_db()
remove_test_user()
check_web_app()
