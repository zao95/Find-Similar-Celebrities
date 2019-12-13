from modules import star_crawler
from modules import face_crop
from modules import compare
import cv2
import re
from matplotlib import pyplot as plt
import glob

# Setting
db_create = False
ratio = 0.75

# 연예인 db List
star_names = [
    "아이유", "문세윤", "샘오취리", "크리스 에반스", "공유", "양요섭", "카렌 길런", "멧 데이먼", "박진영", "이세돌",
    "홍현희", "이승기", "유재석", "박명수", "강호동", "은지원", "남궁민", "채수빈", "손예진", "박신혜", "송혜교",
    "전지현", "한효주", "김고은", "공효진", "김수현", "현빈", "봉준호", "김남길", "이종석", "서경석", "박보검",
    "이동욱", "봉준호", "이정재", "이성재", "유오성", "한석규", "류승범", "정우성", "조승우", "김상경", "감우성",
    "주진모", "최민식", "임창정", "권상우", "장동건", "김수로", "신현준", "이범수", "박용우", "임하룡", "성동일",
    "이병헌", "박중훈", "하정우", "황정민", "정운택", "허준호", "차태현", "정준호", "박철민", "이준기", "강동원",
    "박해일", "정진영", "엄태웅", "이문식", "신하균", "차승원", "공형진", "이한위", "김광규", "원빈", "변희봉",
    "오달수", "김윤석", "성지루", "안성기", "정재영", "설경구", "송강호", "유해진", "손예진", "김혜수", "하지원",
    "엄정화", "김윤진", "한효주", "고아성", "김수미", "심은경", "배두나", "엄지원", "임수정", "김해숙", "송해",
    "박신혜", "김향기", "김수안", "정유미", "나문희", "박보영",
]


def crawling():
    star_crawler.star_crawler(star_names)


def cropping():
    original_file_list = glob.glob("images/*/*")
    for i in original_file_list:
        face_crop.face_crop(i.replace("\\", "/"))


def comparing(image):
    global ratio
    cImg = compare.CompareImg()
    cImg.dist_change(ratio)
    crop_file_list = glob.glob("cropImages/*/*")
    res_data_list = []
    for i in crop_file_list:
        i = i.replace("\\", "/")
        res_data_list.append(cImg.run("./" + str(i), image))
    return crop_file_list[res_data_list.index(max(res_data_list))]


def show(image, target):
    global ratio
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    img_show = cv2.imread(image, 1)
    img_show = cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)
    tar = cv2.imread(target, cv2.IMREAD_GRAYSCALE)
    tar_show = cv2.imread(target, 1)
    tar_show = cv2.cvtColor(tar_show, cv2.COLOR_BGR2RGB)
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(tar, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m,n in matches:
        if m.distance < ratio * n.distance:
            good.append([m])

    knn_image = cv2.drawMatchesKnn(img_show, kp1, tar_show, kp2, good, None, flags=2)
    plt.imshow(knn_image)
    plt.show()


if __name__ == "__main__":
    # 비교 대상 이미지
    target_image = "testImage.jpg"
    target_croping_image = "comparingImage.jpg"

    # 비교 대상 이미지 얼굴 크로핑
    print("비교대상 얼굴 크로핑 작업..", end="")
    face_crop.face_crop(target_image, True)
    print("완료")

    if db_create:
        # 연예인 크롤링 후 images 폴더에 저장
        print("DB 이미지 크롤링 작업..", end="")
        crawling()
        print("완료")

        # 크롤링 이미지를 얼굴만 크로핑해서 cropImages 폴더에 저장
        print("DB 얼굴 크로핑 작업..", end="")
        cropping()
        print("완료")

    # 크롤링 이미지를 목적 이미지와 비교해서 가장 닮은 이미지를 검색
    print("이미지 비교 작업..", end="")
    similar_entertainer = comparing(target_croping_image).replace("\\", "/")
    print("완료")

    # 닮은 연예인 비교 대상과 비교하여 보여주기
    index = re.search("[0-9*]", similar_entertainer)
    print("당신이 가장 닮은 연예인은 ", end="")
    print(star_names[int(similar_entertainer[index.span()[0]:index.span()[1]+1])], end="")
    print("입니다.")
    show(similar_entertainer, target_croping_image)
