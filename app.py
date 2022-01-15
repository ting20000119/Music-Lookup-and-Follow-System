import sqlite3
from flask import Flask, render_template
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('jam.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/register/<string:mid>/<string:mname>/<string:mbirth>/<string:mgender>/<string:mcountry>', methods=['GET'])
def register(mid, mname, mbirth, mgender, mcountry):
    conn = get_db_connection()
    db = conn.cursor()
    uni = db.execute('SELECT * FROM member WHERE mid = ?', [mid]).fetchall()
    conn.commit()
    if not uni:
        db.execute('INSERT INTO member (mid,mname,mbirth,mgender,mcountry) VALUES (?,?,?,?,?)',
                   (mid, mname, mbirth, mgender, mcountry))
        conn.commit()
        conn.close()
        print("register success")
        return "register success"
    else:
        conn.close()
        print("Already registered")
        return "ID taken!"


@app.route('/listSong/<string:mid>', methods=['GET'])
def songList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join add_list on song.sid = add_list.alsid where add_list.almid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    # print(songs)
    # print(type(songs))
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    return res


@app.route('/listArtist/<string:mid>', methods=['GET'])
def artistList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    artists = db.execute(
        'Select artist.aname,artist.abirth,artist.agender,artist.acountry from artist join follow_artist on artist.aid = follow_artist.faaid where follow_artist.famid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(a) for a in artists]), status=200, mimetype='application/json')
    return res


@app.route('/listSongWriter/<string:mid>', methods=['GET'])
def songWriterList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songwriters = db.execute(
        'Select songwriter.wname,songwriter.wbirth,songwriter.wgender,songwriter.wcountry from songwriter join follow_songwriter on songwriter.wid = follow_songwriter.fswid where follow_songwriter.fsmid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(w) for w in songwriters]), status=200, mimetype='application/json')
    return res


@app.route('/listProducer/<string:mid>', methods=['GET'])
def producerList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songwriters = db.execute(
        'Select producer.pname,producer.pbirth,producer.pgender,producer.pcountry from producer join follow_producer on producer.pid = follow_producer.fppid where follow_producer.fpmid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(w) for w in songwriters]), status=200, mimetype='application/json')
    return res


@app.route('/searchArtist/<string:aname>', methods=['GET'])
def searchArtist(aname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said where artist.aname = ?', [aname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    return res


@app.route('/searchProducer/<string:pname>', methods=['GET'])
def searchProducer(pname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join produce on song.sid = produce.psid join producer on producer.pid = produce.ppid where producer.pname = ?', [pname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    return res


@app.route('/searchSongWriter/<string:wname>', methods=['GET'])
def searchSongWriter(wname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where songwriter.wname = ?', [wname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    return res


@app.route('/searchSong/<string:title>', methods=['GET'])
def searchSong(title):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song where song.title= ?', [title]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    return res


# Delete account
@app.route('/delete/<string:mid>', methods=['GET'])
def delete_account(mid):
    conn = get_db_connection()
    db = conn.cursor()
    result = db.execute(
        'Select member.mid from member where member.mid = ?', [mid]).fetchall()
    conn.commit()
    print(result)
    print(type(result))
    if not result:
        conn.close()
        print("the account is not exist.")
        return "the account is not exist."
    else:
        db.execute('Delete from member where mid = ?', [mid])
        conn.commit()
        conn.close()
        print("successful delete.")
        return "successful delete."


@app.route('/login/<string:mid>', methods=['GET'])
def login(mid):
    conn = get_db_connection()
    db = conn.cursor()
    member = db.execute(
        'Select member.mid,member.mname from member where mid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(m) for m in member]), status=200, mimetype='application/json')
    return res


if __name__ == '__main__':
    app.run(debug=True)
