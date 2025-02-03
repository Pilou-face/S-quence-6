from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Modifier selon le bon chemin
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle de la base de données (à adapter selon la structure du dépôt)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')
    books = []
    if query:
        books = Book.query.filter((Book.title.contains(query)) | (Book.author.contains(query))).all()
    return render_template('search.html', books=books, query=query)

if __name__ == '__main__':
    app.run(debug=True)


                                                                                                                                    
if __name__ == "__main__":
  app.run(debug=True)
