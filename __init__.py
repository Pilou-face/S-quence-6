from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)                                                                                                                  

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/livres', methods=['GET', 'POST'])
def afficher_livres():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee = request.form['annee_publication']
        nouveau_livre = Livre(titre=titre, auteur=auteur, annee_publication=annee)
        db.session.add(nouveau_livre)
        db.session.commit()
    livres = Livre.query.all()
    return render_template('livres.html', livres=livres)

@app.route('/supprimer_livre/<int:id>')
def supprimer_livre(id):
    livre = Livre.query.get_or_404(id)
    db.session.delete(livre)
    db.session.commit()
    return redirect('/livres')

@app.route('/')
def HelloWord():
    return render_template('index.html')

                                                                                                                                    
if __name__ == "__main__":
  app.run(debug=True)
