import cv2
import face_recognition
import numpy as np

group_img_file = "imgs/bhuvan.jpg"

person_imgs = [
    {
        "img": "imgs/abhi.jpg",
        "name": "abhi j"
    },
    {
        "img": "imgs/abhis.jpg",
        "name": "abhi s"
    },
    {
        "img": "imgs/bhuvan.jpg",
        "name": "bhuvan"
    },
    {
        "img": "imgs/mitesh.jpg",
        "name": "mitesh"
    }
]

print("making encoding for provided faces")
for i in person_imgs:
    img = face_recognition.load_image_file(i["img"])
    loc = face_recognition.face_locations(img=img)
    enc = face_recognition.face_encodings(face_image=img, known_face_locations=loc)[0]
    i["enc"] = enc

known_face_encs = [i["enc"] for i in person_imgs]

print(person_imgs[0])

image = face_recognition.load_image_file(group_img_file)
face_locations = face_recognition.face_locations(image)
face_encs = face_recognition.face_encodings(face_image=image, known_face_locations=face_locations)

names = []

print(f"Faces : {len(face_locations)}")

img = cv2.imread(group_img_file)

for enc in face_encs:
    matches = face_recognition.compare_faces(known_face_encs, enc, tolerance=0.5)
    print(matches)
    name = "Unknown"
    face_distance = face_recognition.face_distance(known_face_encs, enc)
    best_match_idx = np.argmin(face_distance)
    if(matches[best_match_idx]):
        name = person_imgs[best_match_idx]["name"]
    names.append(name)

for (top,right,bottom,left),n in zip(face_locations,names):
    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, n, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


cv2.imshow("img", img)
cv2.waitKey(0)

