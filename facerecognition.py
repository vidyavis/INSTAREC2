import os
import cv2
import numpy as np
from speech import voice
def detect_face(img, multi=False):
    # convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # load OpenCV face detector, I am using LBP which is fast
    # there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    # let's detect multiscale (some images may be closer to camera than others) images
    # result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    if (len(faces) == 0):
        return None, None

    if multi:
        return faces
    else:
        (x, y, w, h) = faces[0]
        return gray[y:y + w, x:x + h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)

    faces = []
    labels = []

    for dir_name in dirs:

        if not dir_name.startswith("s"):
            continue;
        label = int(dir_name.replace("s", ""))

        subject_dir_path = data_folder_path + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:

            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)

            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels


# print("Preparing data...")
# faces, labels = prepare_training_data("training-data")
# print("Data prepared")
#
# print("Total faces: ", len(faces))
# print("Total labels: ", len(labels))

# face_recognizer.train(faces, np.array(labels))
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

def trainall():
    global face_recognizer
    print("Preparing data...")
    faces, labels = prepare_training_data("training-data")
    print("Data prepared")

    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.train(faces, np.array(labels))


def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img, names):
    global face_recognizer
    img = test_img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_face(img, True)
    print(faces)

    for rect in faces:
        (x, y, w, h) = rect
        face = gray[y:y + w, x:x + h]
        label, confidence = face_recognizer.predict(face)
        print(label, confidence)

        if confidence < 60:
            print(label)
            mark_face(img, label, rect, names)
        else:
            mark_face(img, 0, rect, names)

    return img

def mark_face(img, label, rect, names):
    if label != 0:
        s_text = names[label]
        label_text = 'Detected'
    else:
        label_text = 'Unknown Person'
    voice(s_text)
    print(label_text)
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1] - 5)

    # print("Predicting images...")

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     try:
#         frame = predict(frame)
#     except Exception:
#         pass
#     cv2.imshow("User", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


def predictall( finish, names):
    print("Predicting images...")
    print(names)
    cap = cv2.VideoCapture(0)
    while not finish():
        ret, frame = cap.read()
        try:
            frame = predict(frame,names)
        except Exception:
            pass
        cv2.imshow("User", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
# test_img1 = cv2.imread("test-data/6.jpg")
# test_img2 = cv2.imread("test-data/_84489592_tom1.jpg")
#
# predicted_img1 = predict(test_img1)
# predicted_img2 = predict(test_img2)
# print("Prediction complete")
#
# cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))
# cv2.imshow(subjects[2], cv2.resize(predicted_img2, (400, 500)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
# cv2.destroyAllWindows()
