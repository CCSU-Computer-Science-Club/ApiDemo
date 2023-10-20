from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": "Hello, {}!".format(name)})

if __name__ == "__main__":
    app.run()