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
    status = delete(role_id=role_id)
    return {
        "status": status
    }

@router.post("/create-student")
def create_student(student: Student):
    doc = create(student=student)
    return {
        "status": True,
        "data": doc
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
    student_update = update(student=Student(**student_update))
    return {
        "status": True,
        "data": student_update
    }
