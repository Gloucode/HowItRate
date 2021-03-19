from flask import Flask, render_template
from firebase import firebase
from firebase_admin import db
from flask import request

FBConn = firebase.FirebaseApplication('https://howitrate-user-db-default-rtdb.firebaseio.com/', None)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    category = request.form

    data_to_upload = {
        'Category' : category
    }

    result = FBConn.post('/MyTestData/', data_to_upload)

    return render_template("index.html",result=category)

@app.route('/categories', methods=['POST'])
def categories():

    #Getting data from database
    cats = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/MyTestData', '')

    cat = []

    #looping over dictionary to get categories and put in list
    for i in cats:
        cat.append(cats.get(i).get('Category').get('Category'))

    cat = set(cat)

    return render_template("categories.html", result=cat)

  #return 'Click.'

if __name__ == '__main__':
    app.run(debug=True)






























#bottom
