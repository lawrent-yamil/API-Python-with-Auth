from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye"),
    "lawrent": generate_password_hash("siu")
}

# Auth
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


# Routes
@app.route('/auth', methods=['POST'])
@auth.login_required
def login():
    if verify_password(request.authorization.username, request.authorization.password):
        return "Bienvenido {} a mi api unu".format(request.authorization.username)
    return "Bad credentials", 401

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)