import face_recognition
import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

face_locations = []
face_encodings = []
face_names = []


def recognition(known_face_encodings, known_face_names, is_attendance,
                process_this_frame, recordingFrameView):

    flag, frame = recordingFrameView.cap.read()
    show = cv2.resize(frame,  (0, 0), fx=1.25, fy=1)
    rgb_small_frame = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

       # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings,
                                                    face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                # record whether attendance
                is_attendance[best_match_index] = 1
                # print("Attendance " + name)

            face_names.append(name)
    # print(face_names)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 1
        right *= 1
        bottom *= 1
        left *= 1

        # Draw a box around the face
        cv2.rectangle(rgb_small_frame, (left, top), (right, bottom), (255, 0, 0), 2)
        # Draw a label with a name below the face
        cv2.rectangle(rgb_small_frame, (left, bottom - 35), (right, bottom), (255, 0, 0),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(rgb_small_frame, name, (left + 6, bottom - 6), font, 1.0,
                    (255, 255, 255), 1)

    # Put the video image into UI recording frame
    showImage = QImage(rgb_small_frame.data, rgb_small_frame.shape[1], rgb_small_frame.shape[0], QImage.Format_RGB888)
    recordingFrameView.camera_label.setPixmap(QPixmap.fromImage(showImage))

    if len(face_names) != 0:
        return face_names, is_attendance
    else:
        return [], is_attendance
