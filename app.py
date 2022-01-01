import sqlite3
from flask import Flask, render_template
import json
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
    posts = conn.execute(
        'INSERT INTO MEMBER (MID,MNAME,MBIRTH,MGENDER,MCOUNTRY) VALUES (?,?,?,?,?)', (here))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/listSong/<string:mid>', methods=['GET'])
def songList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join add_list on song.sid = add_list.alsid where add_list.almid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


'''@app.route('/listArtist/<string:mid>', methods=['GET'])
def artistList(mid):
    

@app.route('/listSongWriter/<string:mid>', methods=['GET'])
def songWriterList(mid):
    

@app.route('/listProducer/<string:mid>', methods=['GET'])
def producerList(mid):'''


@app.route('/searchArtist/<string:aname>', methods=['GET'])
def searchArtist(aname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said where artist.aname = ?', [aname]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


# Delete account


def delete_account():
    conn = get_db_connection()
    enter_memID = input('enter member id: ')
    posts = conn.execute('DELETE * FROM MEMBER WHERE MID = ?', (enter_memID))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)
# login


def login():
    conn = get_db_connection()
    enter_memID = input('enter member id: ')
    posts = conn.execute('SELECT * FROM MEMBER WHERE MID = ?', (enter_memID))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
