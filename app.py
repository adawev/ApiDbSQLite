import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Database connection
con = sqlite3.connect("users.db", check_same_thread=False)
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS usersAll (firstName text, lastName text, phone text)")
con.commit()


@app.route("/api/users" , methods=['GET'])
def get_users():
    cur.execute("SELECT * FROM usersAll")
    users = cur.fetchall()

    users_list = [{"firstName": u[0], "lastName": u[1], "phone": u[2]} for u in users]
    return jsonify(users_list), 200

@app.route("/api/users", methods=['POST'])
def create_user():
    data  = request.get_json()

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    phone = data.get("phone")

    cur.execute("INSERT INTO usersAll(firstName, lastName, phone) VALUES (?, ?, ?)",(firstName, lastName, phone))
    con.commit()

    return jsonify({
        "message": "User created successfully",
    }), 201


if __name__ == '__main__':
    app.run(port=4200, debug=True)
