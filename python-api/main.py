from flask import Flask, request, jsonify

app = Flask(__name__) # create an app

@app.route("/") # default root, use the app name (app in this case)
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)