from firebase import firebase
from firebase_admin import db
import flask
import json

FBConn = firebase.FirebaseApplication('https://howitrate-user-db-default-rtdb.firebaseio.com/', None)
#ref = db.reference('https://howitrate-user-db-default-rtdb.firebaseio.com/')

'''while True:
    category = input('Category: ')

    data_to_upload = {
        'Category' : category
    }

    result = FBConn.post('/MyTestData/', data_to_upload)

    #print(result)
    break'''

res = FBConn.get('https://howitrate-user-db-default-rtdb.firebaseio.com/MyTestData', '')

cat = []

for i in res:
    cat.append(res.get(i).get('Category').get('Category'))

    #print(res.get(i).get('Category').get('Category'))

print(cat)







#print(json.dumps(res, indent=1))
