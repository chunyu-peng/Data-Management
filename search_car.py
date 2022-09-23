import firebase_admin
from firebase_admin import db
import re
import sys

cred_obj = firebase_admin.credentials.Certificate('./hw1firebase-bf37e-firebase-adminsdk-qxgsn-05de707d1a.json')
default_app = firebase_admin.initialize_app(cred_obj,
                                            {'databaseURL': 'https://hw1firebase-bf37e-default-rtdb.firebaseio.com'})
input_tokens = re.split('\\W+', sys.argv[1])
for i in range(0, len(input_tokens) - 1):
    if input_tokens[i] == '':
        input_tokens.remove('')
ref = db.reference("/create_index")
if len(input_tokens) == 1:
    if ref.child(input_tokens[0]).get() is None:
        print("No cars found")
    else:
        print(ref.child(input_tokens[0]).get())
    exit()
dup = {}
out = []
for token in input_tokens:
    if token == '':
        continue
    token = token.lower()
    car_IDs = ref.child(token).get()
    if car_IDs is None:
        continue
    for car_ID in car_IDs:
        if car_ID not in dup:
            dup[car_ID] = 0
        dup[car_ID] += 1
dup = dict(sorted(dup.items(), key=lambda item: item[1], reverse=True))
for car_ID in dup.keys():
    out.append(car_ID)
if len(out) == 0:
    print("No cars found")
    exit()
print("IDs of the car are:")
print(out)
