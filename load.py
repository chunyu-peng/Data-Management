import csv
import firebase_admin
from firebase_admin import db
import sys

cred_obj = firebase_admin.credentials.Certificate('./hw1firebase-bf37e-firebase-adminsdk-qxgsn-05de707d1a.json')
default_app = firebase_admin.initialize_app(cred_obj,
                                            {'databaseURL': 'https://hw1firebase-bf37e-default-rtdb.firebaseio.com'})
file_path = sys.argv[1]
file = open('./' + file_path)
info = []
header = next(csv.reader(file))
reader = csv.DictReader(file, header)
for row in reader:
    info.append(row)
ref = db.reference('/load')
ref.set(info)
file.close()
