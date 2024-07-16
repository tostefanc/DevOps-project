import pymysql
from db_secrets import DB_HOST, DB_PORT, DB_USER, DB_SCHEMA, DB_PASSWORD
import time


def create_user(user_id, user_name):
    """
    Inserts in the database a user id and username
    :param user_id:
    :param user_name:
    :return:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    creation_date = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = db_connection.cursor()
    cursor.execute(
        f"INSERT INTO users (id, name, creation_date) VALUES ('{user_id}', '{user_name}', '{creation_date}')")
    cursor.close()
    db_connection.close()


def get_user_data(user_id):
    """
    Gets the username and the id of the user by searching in the DB for the user_id
    :param user_id:
    :return user_data:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT id, name FROM users WHERE ID = '{user_id}'")
    user_data = cursor.fetchall()
    # print(user_data)
    cursor.close()
    db_connection.close()
    return user_data


def modify_user_data(user_id, user_name):
    """
    Modifies the name of the user using the ID
    :param user_id:
    :param user_name:
    :return:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    cursor = db_connection.cursor()
    cursor.execute(f"UPDATE users SET name='{user_name}' where id='{user_id}'")
    cursor.close()
    db_connection.close()


def remove_user(user_id):
    """
    Removes the user that with the user_id ID
    :param user_id:
    :return:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    cursor = db_connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE id='{user_id}'")
    cursor.close()
    db_connection.close()


def table_initialization(table_name):
    """
    Creates the table in the schema
    :param table_name:
    :return:
    """
    db_connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db=DB_SCHEMA)
    db_connection.autocommit(True)
    cursor = db_connection.cursor()
    cursor.execute(
        f"CREATE TABLE `{DB_SCHEMA}`.`{table_name}` (`id` INT NOT NULL, `name` VARCHAR(50) NOT NULL, `creation_date` VARCHAR(50), PRIMARY KEY (`id`))")
