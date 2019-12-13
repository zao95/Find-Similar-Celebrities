import cv2
from study import study05_make_path
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img_path = study05_make_path.make_path("./testImages/test2.jpg")
image = cv2.imread(img_path)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

faces = face_cascade.detectMultiScale(image, 1.03, 5)
if len(faces) == 0:
    print("ERROR : 얼굴 못찾음")

cropped = []
count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped.append(image[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)])
for i in cropped:
    if i.all():
        cv2.imwrite("testimage-" + str(count) + ".png", i)
        count += 1
    break

cv2.rectangle(image, (0, image.shape[0] - 25),
              (270, image.shape[0]), (255,255,255), -1)
cv2.putText(
    image,
    "PinkWink test", (0, image.shape[0] - 10),
    cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0, 0, 0), 1
)

plt.figure(figsize=(12,12))
plt.imshow(i, cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

print(faces.shape)
print("Number of faces detected: " + str(faces.shape[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()