import csv
import re
import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('./hw1firebase-bf37e-firebase-adminsdk-qxgsn-05de707d1a.json')
default_app = firebase_admin.initialize_app(cred_obj,
                                            {'databaseURL': 'https://hw1firebase-bf37e-default-rtdb.firebaseio.com'})
file = open('./cars.csv')
csv_reader = csv.reader(file)
header = next(csv_reader)
index_CarName = header.index("CarName")
index_car_ID = header.index("car_ID")
search_dict = {}
for row in csv_reader:
    for token in re.split('\\W+', row[index_CarName]):
        if token == '':
            continue
        token = token.lower()
        if token not in search_dict:
            search_dict[token] = []
        search_dict[token].append(row[index_car_ID])
ref = db.reference("/create_index")
ref.set(search_dict)
file.close()
