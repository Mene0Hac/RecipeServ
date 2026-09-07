import sqlQuery
from flask import Flask, Blueprint, jsonify


app = Flask(__name__)

get_bp = Blueprint('get', __name__)

def test_route():
    rows=sqlQuery.get_all_users()
    for row in rows:
        print(f"ID: {row.id}, Имя: {row.name}, Возраст: {row.age}")
        
    

@get_bp.route('/get_all_users', methods=['GET'])
def get_all_users_route():
    users = sqlQuery.get_all_users()

    return jsonify([
        {
            "id": user.id,
            "name": user.name,
            "age": user.age
        }
        for user in users
    ])


app.register_blueprint(get_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)