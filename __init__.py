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

@app.route('/')
def HelloWord():
    return render_template('index.html')

                                                                                                                                    
if __name__ == "__main__":
  app.run(debug=True)
