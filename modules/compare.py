import cv2


class CompareImg:
    def __init__(self):
        self.dist = 1
        self.res = -1
        pass

    def dist_change(self, dist_val):
        self.dist = dist_val

    def read_img(self, filepath):
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        return img

    def diff_img(self, img1, img2):
        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good = []
        for m, n in matches:
            if m.distance < self.dist * n.distance:
                good.append([m])
        self.res = len(good)

    def run(self, file1, file2):
        filepath1 = file1
        filepath2 = file2

        img1 = self.read_img(filepath1)
        img2 = self.read_img(filepath2)
        if img2 is None:
            print("ERROR : 대상 이미지 없음")
            return -1
        if img1 is None:
            print("ERROR : db 이미지 없음")
            return -1

        self.diff_img(img1, img2)

        return self.res


if __name__ == '__main__':
    cImg = CompareImg()
    print(cImg.run("./testImages/a.jpg", "./testImages/b.jpg"))