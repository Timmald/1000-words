import base64
from datetime import datetime
from flask import *
import sqlite3
from reverseImageSearch import *
from thesaurus import *

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('QueryRecords')
    conn.row_factory = sqlite3.Row
    return conn


def get_most_recent_entry(entries: list[sqlite3.Row]):
    minTime = None
    for entry in entries:
        time = datetime.strptime(entry['Time'], '%c')
        if minTime is None:
            minTime = time
        elif time > minTime:
            minTime = time
    return minTime.strftime('%c')

@app.route('/', methods=('GET', 'POST'))
def homePage():
    if request.method == 'POST':
        imgUrl = None
        fileAttached = True
        try:
            request.files['img']
        except KeyError:
            fileAttached = False
        if fileAttached:
            img = request.files['img']
            curTime = datetime.now().strftime('%c')
            imgUrl = request.base_url
            imgBytes = bytes(img.stream.read())
            img.close()
        else:
            curTime = datetime.now().strftime('%c')
            imgUrl = request.form['imgUrl']
            imgBytes = None
        conn = get_db_connection()
        conn.execute('INSERT INTO Queries (Time, ImgUrl, Img) VALUES (?, ?, ?)', (curTime, imgUrl, imgBytes))
        conn.commit()
        desc = get_elements_from_img(imgUrl) #TODO: Doesn't work for files until deployed. Deploy.
        corpus = get_corpus_from_desc(desc)
        wikiWords = get_important_words(corpus, 150)
        thouWords = get_thousand_words(wikiWords)
        entries = conn.execute('SELECT * FROM Queries').fetchall()
        conn.execute('UPDATE Queries SET Description=? Corpus=? WikiWords=? 1000Words=? WHERE Time=?', (desc, corpus,wikiWords, thouWords, get_most_recent_entry(entries)))
        conn.commit()
        conn.close()
        return render_template('index.html', thouWords=thouWords)
    return render_template('index.html', thouWords=[])


@app.route('/file/<string:fileName>')
def getFile(fileName: str):
    conn = get_db_connection()
    fileBytes = conn.execute('SELECT Img FROM Queries WHERE ImgUrl = ?', (request.base_url,)).fetchone()['Img']
    fileBytes = base64.b64encode(fileBytes)
    return fileBytes
        #render_template('View_Image.html', fileBytes=fileBytes, filename=fileName)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
