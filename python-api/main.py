from flask import Flask, request, jsonify

app = Flask(__name__) # create an app

@app.route("/") # default route, use the app name (app in this case)
def home():
    return "Home"

@app.route("/get-user/<user_id>") # route for fetching user info
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Jane Doe",
        "email": "jane.doe@email.com"
    }

    extra = request.args.get("extra") # value of extra in the, request variable, args dictionary
    if extra: # if extra exists
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)