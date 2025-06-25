from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# --- Initialize DB ---
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'incomplete'
                )''')
    conn.commit()
    conn.close()

# --- Home Route ---
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# --- Add Task ---
@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO tasks (content) VALUES (?)', (content,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# --- Mark Complete ---
@app.route('/complete/<int:task_id>')
def complete(task_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET status="complete" WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# --- Delete Task ---
@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
