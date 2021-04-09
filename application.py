from flask import Flask, render_template
from firebase import firebase
from firebase_admin import db
from flask import request

#"{{ url_for('handle_data') }}" //instead of typing out entire url

FBConn = firebase.FirebaseApplication('https://howitrate-user-db-default-rtdb.firebaseio.com/', None)

application = Flask(__name__)

categories = []

application.static_folder = 'static'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/', methods=['POST'])
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

@application.route('/categories', methods=['POST'])
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
'''@app.route('/coffeereviews', methods=['POST'])
def coffeereviews():

    #Get anbd display reviews
    #Firebase has buiilt in try and excepts to catch errors
    try:
        reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/Reviews', '')
    except:
        print("It seems as though firebase is down")
        return render_template("coffeereviews.html", result=reviews_l)

    reviews_l = []

    for i in reviews:
        reviews_l.append(reviews.get(i).get('Review').get('review'))
    #print(reviews_l)

    return render_template("coffeereviews.html", result=reviews_l)'''

#where to go to post review about coffee
@application.route('/coffee', methods=['POST'])
def coffee():
    #get the reviews for coffee from the database
    try:
        reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/Reviews', '')
    except Exception:
        #If it cannot then go back to home page
        print("It seems as though firebase is down")
        return render_template("index.html")

    reviews_l = []
    names_l = []
    if (reviews != None):
        for i in reviews:
            reviews_l.append(( reviews.get(i).get('Review') , reviews.get(i).get('Name') ))

    #Retrieve Review
    rev = request.form.get('ratDesc')
    name =  request.form.get('ratCatName')

    #Create user review into dictionary
    rev_to_upload = {
        'Review' : rev,
        'Name' : name
    }
    #Post to firebase
    FBConn.post('/Reviews/', rev_to_upload)


    return render_template("coffee.html", result=reviews_l)


#where to go to review food
@application.route('/food', methods=['POST'])
def food():
    #get the reviews for coffee from the database
    try:
        reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/FoodReviews', '')
    except Exception:
        #If it cannot then go back to home page
        print("It seems as though firebase is down...")
        return render_template("index.html")

    reviews_l = []
    names_l = []
    if (reviews != None):
        for i in reviews:
            reviews_l.append(( reviews.get(i).get('Review') , reviews.get(i).get('Name') ))

    #Retrieve Review
    rev = request.form.get('ratDesc')
    name =  request.form.get('ratCatName')

    #Create user review into dictionary
    rev_to_upload = {
        'Review' : rev,
        'Name' : name
    }
    #Post to firebase
    FBConn.post('/FoodReviews/', rev_to_upload)


    return render_template("food.html", result=reviews_l)


#where to go to review wine
@application.route('/wine', methods=['POST'])
def wine():
    #get the reviews for coffee from the database
    try:
        reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/WineReviews', '')
    except Exception:
        #If it cannot then go back to home page
        print("It seems as though firebase is down...")
        return render_template("index.html")

    reviews_l = []
    names_l = []
    if (reviews != None):
        for i in reviews:
            reviews_l.append(( reviews.get(i).get('Review') , reviews.get(i).get('Name') ))

    #Retrieve Review
    rev = request.form.get('ratDesc')
    name =  request.form.get('ratCatName')

    #Create user review into dictionary
    rev_to_upload = {
        'Review' : rev,
        'Name' : name
    }
    #Post to firebase
    FBConn.post('/WineReviews/', rev_to_upload)


    return render_template("wine.html", result=reviews_l)


#where to go to review shoes
@application.route('/shoes', methods=['POST'])
def shoes():
    #get the reviews for coffee from the database
    try:
        reviews = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/ShoesReviews', '')
    except Exception:
        #If it cannot then go back to home page
        print("It seems as though firebase is down...")
        return render_template("index.html")

    reviews_l = []
    names_l = []
    if (reviews != None):
        for i in reviews:
            reviews_l.append(( reviews.get(i).get('Review') , reviews.get(i).get('Name') ))

    #Retrieve Review
    rev = request.form.get('ratDesc')
    name =  request.form.get('ratCatName')

    #Create user review into dictionary
    rev_to_upload = {
        'Review' : rev,
        'Name' : name
    }
    #Post to firebase
    FBConn.post('/ShoesReviews/', rev_to_upload)


    return render_template("shoes.html", result=reviews_l)

if __name__ == '__main__':
    application.run(debug=True)


'''<form action="http://localhost:5000/categories" method="POST">
<p><input type="submit" name= "form" value={{cat}}></p>
</form>'''



#bottom
