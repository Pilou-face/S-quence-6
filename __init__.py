from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'  # Modifier selon le bon chemin

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL)''')
    cursor.executemany('''INSERT INTO books (title, author) VALUES (?, ?)''', [
        ('Le Petit Prince', 'Antoine de Saint-Exupéry'),
        ('1984', 'George Orwell'),
        ('Les Misérables', 'Victor Hugo'),
        ('Harry Potter à l'école des sorciers', 'J.K. Rowling'),
        ('L'Étranger', 'Albert Camus')]''')
    conn.commit()
    conn.close()

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
    init_db()
    app.run(debug=True)
