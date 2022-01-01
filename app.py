import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('jam.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/register')
def register():
    conn = get_db_connection()
    posts = conn.execute('INSERT INTO MEMBER (MID,MNAME,MBIRTH,MGENDER,MCOUNTRY) VALUES (?,?,?,?,?)', (here))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)

# Delete account
def delete_account():
    conn = get_db_connection()
    enter_memID = input('enter member id: ')
    posts = conn.execute('DELETE * FROM MEMBER WHERE MID = ?',(enter_memID))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)
# login
def login():
    conn = get_db_connection()
    enter_memID = input('enter member id: ')
    posts = conn.execute('SELECT * FROM MEMBER WHERE MID = ?',(enter_memID))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)
if __name__ == '__main__':
    app.run(debug=True)
