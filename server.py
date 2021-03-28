from flask import Flask, render_template
from firebase import firebase
from firebase_admin import db
from flask import request

#"{{ url_for('handle_data') }}" //instead of typing out entire url

FBConn = firebase.FirebaseApplication('https://howitrate-user-db-default-rtdb.firebaseio.com/', None)

app = Flask(__name__)

categories = []

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    category = request.form.get('catName')

    data_to_upload = {
        'Category' : category
    }

    result = FBConn.post('/MyTestData/', data_to_upload)

    return render_template("index.html",result=category)

'''@app.route('/addreview', methods=['POST'])
def addreview():
    review = request.form['Review']

    data_to_upload = {
        'Review' : review
    }

    result = FBConn.post('/Reviews/', data_to_upload)'''

@app.route('/categories', methods=['POST'])
def categories():

    #Getting data from database
    cats = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/MyTestData', '')

    cat = []

    #looping over dictionary to get categories and put in list
    for i in cats:
        cat.append(cats.get(i).get('Category'))

    print(cat)

    cat = set(cat)
    cat = sorted(cat)

    return render_template("categories.html", result=cat)

  #return 'Click.'

#where coffee reviews are
@app.route('/coffeereviews', methods=['POST'])
def coffeereviews():

    #Get anbd display reviews
    reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/Reviews', '')

    reviews_l = []

    for i in reviews:
        reviews_l.append(reviews.get(i).get('Review').get('review'))
    #print(reviews_l)

    return render_template("coffeereviews.html", result=reviews_l)

#where to go to post review about coffee
@app.route('/coffee', methods=['POST'])
def coffee():
    reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/Reviews', '')
    #whenever coffee button is pressed it is added to database, have to fix
    reviews_l = []
    names_l = []
    print(reviews)
    if (reviews != None):
        for i in reviews:
            print(reviews.get(i).get('Reviews').get('Review'))
            reviews_l.append(reviews.get(i).get('Reviews').get('Review'))
            names_l.append(reviews.get(i).get('Reviews').get('Name'))

    #Retrieve Review
    rev = request.form.get('ratDesc')
    name =  request.form.get('ratCatName')

    
    rev_to_upload = {
        'Review' : rev,
        'Name' : name
    }
    FBConn.post('/Reviews/', rev_to_upload)
    

    return render_template("coffee.html", result=reviews_l)

if __name__ == '__main__':
    app.run(debug=True)


'''<form action="http://localhost:5000/categories" method="POST">
<p><input type="submit" name= "form" value={{cat}}></p>
</form>'''






























#bottom
