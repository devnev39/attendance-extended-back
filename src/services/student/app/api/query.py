from firebase_admin.firestore import firestore
from src.db.db import db
from src.services.student.app.api.model import Student

default_collection = "students"

def create(student : Student):
    doc_ref = db.collection(default_collection).document(student.role_id)
    doc_ref.set(student.__dict__)
    doc = get(role_id=student.role_id)
    return doc

def delete(role_id: str):
    db.collection(default_collection).document(role_id).delete()
    return True

def get_all():
    docs = db.collection(default_collection).stream()
    return [doc.to_dict() for doc in docs]

def get(role_id):
    docs = db.collection(default_collection).where(filter= firestore.FieldFilter("role_id","==",role_id)).stream()
    docs = [doc.to_dict() for doc in docs]
    return docs[0] if len(docs) else None

def update(student: Student, role_id):
    doc_ref = db.collection(default_collection).document(role_id)
    doc_ref.set(student.__dict__)
    doc = get(role_id=role_id)
    return doc
