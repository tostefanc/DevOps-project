import os
import signal
from flask import Flask
from db_connector import get_user_data

app = Flask(__name__)


@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    """
    Displays the username by using the ID
    If the ID does not exist it displays an error
    :param user_id:
    :return HTML h1 tag containing user name or error:
    """
    user = get_user_data(user_id)
    if len(user) == 0:
        return f"<h1 id='error'> no such user {user_id} </h1>", 404
    return f"<h1 id='user'> {user[0][1]} </h1>"


@app.route('/stop_server')
def stop_server():
    if os.name == 'posix':
        os.kill(os.getpid(), signal.SIGINT)
    if os.name == 'nt':
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def route_not_found(e):
    return f"<h2 style=\"color:blue;\">Path not found </h2>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
