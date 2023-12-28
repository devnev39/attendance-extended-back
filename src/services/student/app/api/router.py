import face_recognition
from fastapi import APIRouter, UploadFile, File
from src.services.student.app.api.query import get, create, delete, get_all, update
from src.services.student.app.api.model import Student
from src.db.db import bucket

router = APIRouter()

@router.get("/get-students")
def get_students():
    data = get_all()
    return {
        "status": True,
        "data": data
    }

@router.delete("/delete-students")
def delete_student(role_id: str):
    student = get(role_id=role_id)
    status = delete(role_id=role_id)
    name = student["photoid_url"].split("/")[-1]
    bucket.delete_blob(f'student_ids/{name}')
    return {
        "status": status
    }

def make_encoding(img):
    i = face_recognition.load_image_file(img)
    locs = face_recognition.face_locations(img=i)
    img = face_recognition.face_encodings(face_image=i, known_face_locations=locs)[0]
    return img.tolist()

@router.post("/create-student")
def create_student(
    role_id: str,
    name: str,
    file: UploadFile
):
    try:
        filename = f'{role_id}.{file.filename.split(".")[-1]}'
        blob = bucket.blob(f'student_ids/{filename}')
        blob.upload_from_file(file_obj=file.file)
        blob.make_public()
        doc = Student(role_id=role_id, name=name, photoid_url=blob.public_url, encoding=make_encoding(file.file))
        doc = create(doc)
        return {
            "status": True,
            "data": doc
        }
    except Exception as ex:
        print(ex)
        return {
            "status": False,
            "message": str(ex)
        }

@router.post("/upload-student-pic")
def upload_student_pic(
    role_id: str,
    file: UploadFile
):
    filename = f'{role_id}.{file.filename.split(".")[-1]}'
    blob = bucket.blob(f'student_ids/{filename}')
    blob.upload_from_file(file_obj=file.file)
    blob.make_public()
    student_update = get(role_id=role_id)
    student_update["photoid_url"] = blob.public_url
    student_update = update(student=Student(**student_update), role_id=role_id)
    return {
        "status": True,
        "data": student_update
    }
