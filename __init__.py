from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'  # Modifier selon le bon chemin

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')
    books = []
    if query:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + query + '%', '%' + query + '%'))
        books = cursor.fetchall()
        conn.close()
    return render_template('search.html', books=books, query=query)

if __name__ == '__main__':
    app.run(debug=True)

