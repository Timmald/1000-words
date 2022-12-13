from flask import *
from reverseImageSearch import *
from requests import get

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def homePage():
    if request.method == 'POST':
        pass
        # if there are files
        # TODO: get files uploaded from request.files, use filename and stream attrs
        # call uploadImage and put new urls and bytes in db
        # then
        # do the things and add to db at each step


    return render_template('index.html')

#TODO: Write a new route for accessing images by url in the database
if __name__ == '__main__':
    app.run()
