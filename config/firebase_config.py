import firebase_admin
from firebase_admin import credentials,firestore
import os

ROOT_PATH = os.path.abspath(os.getcwd())
print(ROOT_PATH)
5
cred = credentials.Certificate(os.path.join(ROOT_PATH,'heineken-project-541d5-firebase-adminsdk-fbsvc-d9d1fd237c.json'))
app = firebase_admin.initialize_app(cred)
print("Printing the name of the project : ", app.name)
db = firestore.client()
db.collection("test_collection").document("hello world").set({"name":"john"})