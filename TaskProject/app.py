from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Helper functions to interact with the SQLite database
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row  # Allows us to access columns by name
    return conn

def add_task(task_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_name, status) VALUES (?, ?)', (task_name, 'Pending'))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET status = "Completed" WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    tasks = get_tasks()
    return render_template('task_list.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_new_task():
    task_name = request.form['task_name']
    add_task(task_name)
    return redirect(url_for('home'))

@app.route('/complete_task/<int:task_id>')
def mark_completed(task_id):
    complete_task(task_id)
    return redirect(url_for('home'))

@app.route('/delete_task/<int:task_id>')
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)