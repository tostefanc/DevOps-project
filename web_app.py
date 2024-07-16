from flask import Flask
from db_connector import get_user_data

app = Flask(__name__)


@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    user = get_user_data(user_id)
    if len(user) == 0:
        return f"<h1 id='error'> no such user {user_id} </h1>"
    return f"<h1 id='user'> {user[0][1]} </h1>"


app.run(port=5001)
