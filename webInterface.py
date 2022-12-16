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


@app.route('/', methods=('GET', 'POST'))
def homePage():
    if request.method == 'POST':
        imgUrl = None
        if not request.files['img'].content_length == 0:
            img = request.files['img']
            curTime = datetime.now().strftime('%c')
            imgUrl = '/file/' + str(img.filename)
            imgBytes = bytes(img.stream.read())
            img.close()
        else:
            curTime = datetime.now().strftime('%c')
            imgUrl = request.form['imgUrl']
            imgBytes = None
        desc = get_elements_from_img(imgUrl)
        corpus = get_corpus_from_desc(desc)
        wikiWords = get_important_words(corpus, 150)
        thouWords = get_thousand_words(wikiWords)
        conn = get_db_connection()
        conn.execute('INSERT INTO Queries VALUES (?,?,?,?,?,?,?)',(curTime, imgUrl, imgBytes, desc, corpus, json.dumps(wikiWords, indent=0), json.dumps(thouWords, indent=0)))
        conn.commit()
        conn.close()
        return render_template('index.html', thouWords=thouWords)
    return render_template('index.html', thouWords=[])


@app.route('/file/<string:fileName>')
def getFile(fileName:str):
    conn = get_db_connection()
    fileBytes = conn.execute('SELECT Img FROM Queries WHERE ImgUrl = ?', (fileName)).fetchone()['Img']
    return fileBytes

if __name__ == '__main__':
    app.run(port=8000, debug=True)
