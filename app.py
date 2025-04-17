from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
        return "Hello, Flask World!"

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000)
