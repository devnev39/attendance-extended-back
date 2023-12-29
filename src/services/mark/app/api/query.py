from src.db.db import db

def get_all_students():
    docs = db.collection("students").stream()
    docs = [doc.to_dict() for doc in docs]
    return docs

def add_attendance_sequentially(attendance: list, date: str):
    for att in attendance:
        doc_ref = db.collection("attendance").document(date).collection("attendance").document(att["role_id"])
        doc_ref.set(att)
    return True

def get_attendance_dates():
    docs = db.collection("attendance").stream()
    return [doc.to_dict() for doc in docs]

def get_all_attendance(date: str):
    docs = db.collection("attendance").document(date).collection("attendance").stream()
    return [doc.to_dict() for doc in docs]