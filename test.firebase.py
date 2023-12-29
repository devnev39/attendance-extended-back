import datetime
import firebase_admin
from firebase_admin import firestore, storage

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app(
    options= {
        "storageBucket": "attendance-a5c9b.appspot.com"
    }
)
bucket = storage.bucket()
db = firestore.client()
d = str(datetime.datetime.now().date())
db.collection("attendance").document(d).collection("attendance").document("20EL012").set({"role_id": "20EL012"})