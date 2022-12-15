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
        if request.files is not None:
            img = request.files[0]
            curTime = datetime.datetime.now().strftime('%c')
            imgUrl = '/' + str(img.filename)
            imgBytes = bytes(img.stream.read())
            img.close()
        else:
            curTime = datetime.datetime.now().strftime('%c')
            imgUrl = request.form['imgUrl']
            imgBytes = None
        desc = get_elements_from_img(imgUrl)
        corpus = get_corpus_from_desc(desc)
        wikiWords = get_important_words(corpus)
        thouWords = get_thousand_words(wikiWords)
        conn = get_db_connection()
        conn.execute('INSERT INTO Queries * VALUES (?,?,?,?,?,?,?)',(curTime, imgUrl, imgBytes, desc, corpus, wikiWords, thouWords))
        conn.commit()
        conn.close()
        return render_template('index.html', thouWords=thouWords)
    return render_template('index.html', thouWords=[])


# TODO: Write a new route for accessing images by url in the database
if __name__ == '__main__':
    app.run()
