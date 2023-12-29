import numpy as np
import cv2
import face_recognition
from fastapi import APIRouter
from fastapi import UploadFile, File
from src.services.mark.app.api.query import get_all_students, add_attendance_sequentially, get_all_attendance, get_attendance_dates
from src. services.mark.app.api.model import MarkAttendanceModel

router = APIRouter()

@router.post("/check-present")
def mark_attendance(
    image: bytes = File()    
):
    try:
        # Check all the faces in image
        # Return all the students which are matched
        img = cv2.imdecode(np.asarray(bytearray(image),dtype="uint8"),cv2.IMREAD_COLOR)
        students = get_all_students()
        encodings = [s["encoding"] for s in students]
        # img = face_recognition.load_image_file(img)
        locs = face_recognition.face_locations(img=img)
        encs = face_recognition.face_encodings(face_image=img, known_face_locations=locs)
        print("face found : ",len(encs))
        names = []

        for enc in encs:
            matches = face_recognition.compare_faces(encodings, enc, tolerance=0.5)
            print(matches)
            name = "Unknown"
            face_distance = face_recognition.face_distance(encodings, enc)
            best_match_idx = np.argmin(face_distance)
            if(matches[best_match_idx]):
                name = students[best_match_idx]["name"]
                students[best_match_idx]["present"] = True
            names.append(name)
        for s in students:
            s.update({"encoding": None})
            if(s.get("present",0) == 0):
                s.update({"present" : False})
        
        return {
            "status": True,
            "data": students
        }
    except Exception as ex:
        print(ex)
        return {
            "status": False,
            "message": str(ex)
        }
    
@router.post("/mark-attendance")
def mark_attendance(
    attendance: MarkAttendanceModel    
):
    try:
        add_attendance_sequentially(attendance=attendance.attendance, date=attendance.date)
        return {
            "status": True
        }
    except Exception as ex:
        print(ex)
        return {
            "status": False,
            "message": str(ex)
        }

@router.get("/get-dates")
def get_dates():
    result = get_attendance_dates()
    return {
        "status": True,
        "data": result
    }

@router.get("/get-attendance")
def get_attendance(
    date: str
):
    try:
        result = get_all_attendance(date = date)
        return {
            "status": True,
            "data": result
        }
    except Exception as ex:
        print(ex)
        return {
            "status": True,
            "message": str(ex)
        }
