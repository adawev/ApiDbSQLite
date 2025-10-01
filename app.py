import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS


# Database connection
con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS usersAll (firstName text, lastName text, phone text)")
con.commit()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/api/users" , methods=['GET'])
def get_users():
    cur.execute("SELECT * FROM usersAll")
    users = cur.fetchall()

@app.route("/api/users", methods=['POST'])
def create_user():
    data  = request.get_json()

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    phone = data.get("phone")

    cur.execute("INSERT INTO usersAll(first_name, last_name, phone) VALUES (?, ?, ?)", (firstName, lastName, phone))
    con.commit()

    return jsonify({
        "message": "User created successfully",
    }), 201


if __name__ == '__main__':
    app.run(port=4200, debug=True)
