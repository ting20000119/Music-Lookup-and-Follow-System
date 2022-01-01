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
@app.route('/delete')
def delete_account(memID):
    conn = get_db_connection()
    result = conn.execute('DELETE * FROM MEMBER WHERE MID = ?',(memID)).fetchone()
    conn.commit()
    conn.close()
    if result is None:
        return "the account is not exist.";
    else:
        return "successful delete."

# login
@app.route('/login')
def login(memID):
    conn = get_db_connection()
    result = conn.execute('SELECT * FROM MEMBER WHERE MID = ?',(memID)).fetchone()
    conn.close()
    if result is None:
        return None;
    else:
        return (conn.MID , conn.MName)
    
    
if __name__ == '__main__':
    app.run(debug=True)
