import firebase_admin
from firebase_admin import db
import sys

cred_obj = firebase_admin.credentials.Certificate('./hw1firebase-bf37e-firebase-adminsdk-qxgsn-05de707d1a.json')
default_app = firebase_admin.initialize_app(cred_obj,
                                            {'databaseURL': 'https://hw1firebase-bf37e-default-rtdb.firebaseio.com'})
out = []
ref = db.reference("/load")
data = ref.get()
low = sys.argv[1]
high = sys.argv[2]
for i in range(0, len(data) - 1):
    price = ref.child(str(i)).child("price").get()
    if float(low) <= float(price) <= float(high):
        out.append(ref.child(str(i)).child("car_ID").get())
if len(out) == 0:
    print("No cars found with the given range")
    exit()
print("IDs for the car price range are:")
print(out)
