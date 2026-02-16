from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    # fake risk value (later tum model se replace karna)
    risk = random.randint(10, 95)

    return render_template("index.html", risk=risk)

if __name__ == "__main__":
    app.run(debug=True)
