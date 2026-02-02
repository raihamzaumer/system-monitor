from flask import Flask, jsonify, render_template
from monitor import get_system_stats

app = Flask(__name__)

@app.route("/api/stats")
def stats():
    return jsonify(get_system_stats())

@app.route("/")
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
