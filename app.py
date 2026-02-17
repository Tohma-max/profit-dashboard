from flask import Flask, render_template, request, redirect
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DATABASE = "data.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL,
            investment INTEGER NOT NULL,
            return_amount INTEGER NOT NULL,
            profit INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    records = conn.execute("SELECT * FROM records").fetchall()
    conn.close()
    return render_template("index.html", records=records)

@app.route("/add", methods=["POST"])
def add():
    date = request.form["date"]
    category = request.form["category"]
    type_ = request.form["type"]
    investment = int(request.form["investment"])
    return_amount = int(request.form["return"])
    profit = return_amount - investment

    conn = get_db()
    conn.execute(
        "INSERT INTO records (date, category, type, investment, return_amount, profit) VALUES (?, ?, ?, ?, ?, ?)",
        (date, category, type_, investment, return_amount, profit),
    )
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
