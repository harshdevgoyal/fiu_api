import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./aa-fiu-firebase-adminsdk-81i5j-428e2a19e9.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

customers_collection = db.collection('customers')