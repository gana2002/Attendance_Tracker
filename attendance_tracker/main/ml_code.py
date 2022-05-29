import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime



#path of the images which is being written 
path = 'C:/Users/LENOVO/Desktop/final_project/joplay/joplay/attendance_tracker/images'
images = []
personNames = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')      #reading the images in the directory 
    images.append(current_Img)                        #appending the images in the list
    personNames.append(os.path.splitext(cu_img)[0])   #taking the zeroth element(removing jpg from the image)
print(personNames)



#generalised fuction for taking out face encodings 
#(face-recognition is based on dlib implementation which generates 128 measurements from the image)
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #cv2 reads in the format of BGR so converting to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)                   #Appending the encodings 
    return encodeList

#Function to mark the attendance along with the date and time.
# path_attendance = 'Attendance.csv'
path_attendance = 'C:/Users/LENOVO/Desktop/final_project/joplay/joplay/attendance_tracker/templates/attendance.csv'
def attendance(name): 
    with open(path_attendance, 'r+') as f:  
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()  #recording the current date and time 
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tStr},{dStr}<br>')


encodeListKnown = faceEncodings(images)
print('All Encodings Complete!!!')

cap = cv2.VideoCapture(0)
img_counter=0
while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)   #resizing the camera frame 
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)   #finds the face in the current frame 
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  #comapring the faces and the encodings of the frame
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  
        # print(faceDis)
        matchIndex = np.argmin(faceDis)   #finds the index value of the minimum distance 

        if matches[matchIndex]:
            name = personNames[matchIndex].upper()    
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4     #resizing again so as to get the original face 
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED) 
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2) 
            attendance(name)

    cv2.imshow('Webcam', frame)  
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()