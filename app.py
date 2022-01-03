import sqlite3
from flask import Flask, render_template
import json
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('jam.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/register')
def register():
    conn = get_db_connection()
    posts = conn.execute(
        'INSERT INTO MEMBER (MID,MNAME,MBIRTH,MGENDER,MCOUNTRY) VALUES (?,?,?,?,?)', (here))
    conn.commit()
    conn.close()
    return render_template('index.html', posts=posts)


'''@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)'''


@app.route('/listSong/<string:mid>', methods=['GET'])
def songList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join add_list on song.sid = add_list.alsid where add_list.almid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


@app.route('/listArtist/<string:mid>', methods=['GET'])
def artistList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    artists = db.execute(
        'Select artist.aname,artist.abirth,artist.agender,artist.acountry from artist join follow_artist on artist.aid = follow_artist.faaid where follow_artist.famid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(a) for a in artists]), status=200, mimetype='application/json')


@app.route('/listSongWriter/<string:mid>', methods=['GET'])
def songWriterList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songwriters = db.execute(
        'Select songwriter.wname,songwriter.wbirth,songwriter.wgender,songwriter.wcountry from songwriter join follow_songwriter on songwriter.wid = follow_songwriter.fswid where follow_songwriter.fsmid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(w) for w in songwriters]), status=200, mimetype='application/json')


@app.route('/listProducer/<string:mid>', methods=['GET'])
def producerList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songwriters = db.execute(
        'Select producer.pname,producer.pbirth,producer.pgender,producer.pcountry from producer join follow_producer on producer.pid = follow_producer.fppid where follow_producer.fpmid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(w) for w in songwriters]), status=200, mimetype='application/json')


@app.route('/searchArtist/<string:aname>', methods=['GET'])
def searchArtist(aname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said where artist.aname = ?', [aname]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


@app.route('/searchProducer/<string:pname>', methods=['GET'])
def searchProducer(pname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join produce on song.sid = produce.psid join producer on producer.pid = produce.ppid where producer.pname = ?', [pname]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


@app.route('/searchSongWriter/<string:wname>', methods=['GET'])
def searchSongWriter(wname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where songwriter.wname = ?', [wname]).fetchall()
    conn.commit()
    conn.close()
    return app.response_class(response=json.dumps([dict(s) for s in songs]), status=200, mimetype='application/json')


# Delete account
@app.route('/delete')
def delete_account(memID):
    conn = get_db_connection()
    result = conn.execute(
        'DELETE * FROM MEMBER WHERE MID = ?', (memID)).fetchone()
    conn.commit()
    conn.close()
    if result is None:
        return "the account is not exist."
    else:
        return "successful delete."

# login


@app.route('/login')
def login(memID):
    conn = get_db_connection()
    result = conn.execute(
        'SELECT * FROM MEMBER WHERE MID = ?', (memID)).fetchone()
    conn.close()
    if result is None:
        return None
    else:
        return (conn.MID, conn.MName)


if __name__ == '__main__':
    app.run(debug=True)
