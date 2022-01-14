import sqlite3
from flask import Flask, render_template
import json
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('jam.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/listSong/<string:mid>', methods=['GET'])
def songList(mid):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song join add_list on song.sid = add_list.alsid where add_list.almid = ?', [mid]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
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
    res.headers.add('Access-Control-Allow-Origin', '*')
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
    res.headers.add('Access-Control-Allow-Origin', '*')
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
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


# Find songs by this artist's name
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
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


# Test Code ###############
@app.route('/searchArtistTest/<string:aname>', methods=['GET'])
def searchArtistTest(aname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language,artist.aname,producer.pname,songwriter.wname from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said join produce on song.sid = produce.psid  join producer on producer.pid = produce.ppid join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where artist.aname = ?', [aname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/searchProducerTest/<string:pname>', methods=['GET'])
def searchProducerTest(pname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language,artist.aname,producer.pname,songwriter.wname from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said join produce on song.sid = produce.psid  join producer on producer.pid = produce.ppid join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where producer.pname = ?', [pname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/searchSongWriterTest/<string:wname>', methods=['GET'])
def searchSongWriterTest(wname):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language,artist.aname,producer.pname,songwriter.wname from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said join produce on song.sid = produce.psid  join producer on producer.pid = produce.ppid join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where songwriter.wname = ?', [wname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/searchSongTest/<string:title>', methods=['GET'])
def searchSongTest(title):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language,artist.aname,producer.pname,songwriter.wname from song join sing on song.sid = sing.ssid join artist on artist.aid = sing.said join produce on song.sid = produce.psid  join producer on producer.pid = produce.ppid join compose on song.sid = compose.csid join songwriter on songwriter.wid = compose.cwid where song.title = ?', [title]).fetchall()
    conn.commit()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
####################

# Find songs by this producer's name


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
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

# Find songs by this songwriter's name


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
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/searchSong/<string:title>', methods=['GET'])
def searchSong(title):
    conn = get_db_connection()
    db = conn.cursor()
    songs = db.execute(
        'Select song.title,song.genre,song.year,song.language from song where song.title= ?', [title]).fetchall()
    conn.commit()
    res = app.response_class(response=json.dumps(
        [dict(s) for s in songs]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/FindArtist/<string:aname>', methods=['GET'])  # Find this Artist
def FindArtist(aname):
    conn = get_db_connection()
    db = conn.cursor()
    names = db.execute(
        'Select artist.aname,artist.abirth,artist.agender,artist.acountry from artist where artist.aname = ?', [aname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(name) for name in names]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


# Find this Producer
@app.route('/FindProducer/<string:pname>', methods=['GET'])
def FindProducer(pname):
    conn = get_db_connection()
    db = conn.cursor()
    names = db.execute(
        'Select producer.pname,producer.pbirth,producer.pgender,producer.pcountry from producer where producer.pname = ?', [pname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(name) for name in names]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


# Find this songwriter
@app.route('/FindSongWriter/<string:wname>', methods=['GET'])
def FindSongWriter(wname):
    conn = get_db_connection()
    db = conn.cursor()
    names = db.execute(
        'Select songwriter.wname,songwriter.wbirth,songwriter.wgender,songwriter.wcountry from songwriter where songwriter.wname = ?', [wname]).fetchall()
    conn.commit()
    conn.close()
    res = app.response_class(response=json.dumps(
        [dict(name) for name in names]), status=200, mimetype='application/json')
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

# Delete account


@app.route('/delete/<int:memID>', methods=['DELETE'])
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


@app.route('/login/<int:memID>', methods=['GET'])
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
