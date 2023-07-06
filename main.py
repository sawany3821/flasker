from flasker import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = "database.db"

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_firms = con.execute('SELECT * FROM firms').fetchall()
    
    con.close()
    
    firms = []
    for row in db_firms:
        firms.append({'company_name':row[0], 'earning':row[1], 'future_earning':row[2]})

    return render_template(
        'index.html',
        firms=firms
    )
        
@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=["POST"])
def register():
    company_name = request.form['company_name']
    earning = request.form['earning']
    future_earning = request.form['future_earning']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO firms VALUES(?,?,?)',[company_name, earning, future_earning])
    con.commit()
    con.close()
    return redirect(url_for('index'))
