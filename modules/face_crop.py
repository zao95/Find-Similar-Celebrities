import cv2
from study import study05_make_path
import re
import hashlib


def get_hash(file_path, blocksize=65536):
    afile = open(file_path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def face_crop(url, your_face=False):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img_path = study05_make_path.make_path(url)
    image = cv2.imread(img_path)
    try:
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print("ERROR : 이미지 에러")
        print(e)
        return 0

    faces = face_cascade.detectMultiScale(grayImage, 1.03, 5)
    if len(faces) == 0:
        print("work dir : ", end="")
        print(url, end=" // ")
        print("ERROR : 얼굴 못찾음")
    if len(faces) > 1:
        print("work dir : ", end="")
        print(url, end=" // ")
        print("ERROR : 얼굴 인식 2개 이상")

    for (x, y, w, h) in faces:
        cropped = image[y:y + h, x:x + w]

    try:
        t = re.search("\d*.jpg", img_path)
        if your_face is True:
            cv2.imwrite(img_path.replace("testImage", "comparingImage"), cropped)
            return
        print("save dir : ", end="")
        print(img_path.replace("images", "cropImages").replace(img_path[t.span()[0]:], str(get_hash(img_path)[:8]) + ".jpg"))
        cv2.imwrite(img_path.replace("images", "cropImages").replace(img_path[t.span()[0]:], str(get_hash(img_path)[:8]) + ".jpg"), cropped)
    except Exception as e:
        print("ERROR : 저장에러")
        print(e)


if __name__ == "__main__":
    face_crop("../testImages/eri.jpg")
