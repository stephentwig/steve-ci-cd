from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    sum_value = 2 + 2  # Simple computation
    return str(sum_value)

def multiply():
    a = 3
    b = 4
    return a * b

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
