import cv2
from study import study05_make_path

img_path = study05_make_path.make_path("./images/test.jpg")
mp4_path = study05_make_path.make_path("./images/test.mp4")

image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
capture = cv2.VideoCapture(mp4_path)

try:
    height, width, channel = image.shape
    print(height, width, channel)
except Exception as ex:
    height, width = image.shape
    print("image height: " + str(height))
    print("image width: " + str(width))


cv2.imshow("cat", image)
cv2.waitKey(0)

while True:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open(mp4_path)

    ret, frame = capture.read()
    cv2.imshow("steak", frame)

    if cv2.waitKey(33) > 0:
        break

capture.release()
cv2.destroyAllWindows()
