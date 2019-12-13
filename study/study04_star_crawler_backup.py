import os
import requests as re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def input_data(rank, title, artist):
    return {"rank": rank, "title": title, "artist": artist}


# ========== Main part ==========
def star_crawler():
    if __name__ == "__main__":
        source = re.get("https://www.melon.com/chart/index.htm", headers={"User-Agent": "XY"})
        html = BeautifulSoup(source.text, "html.parser")

        star_names = [
            "아이유",
            "문세윤",
            "샘오취리",
            "크리스 에반스",
            "공유",
        ]
        save_names = [
            "IU",
            "Mun_Seyun",
            "Sam_Okyere",
            "Chris_Evan",
            "Gong_Yu",
        ]

        for i in range(0, len(star_names)):
            url_info = "https://www.google.co.kr/search?"
            params = {
                "q": star_names[i],
                "tbm": "isch"
            }
            html_object = re.get(url_info, params)
            if html_object.status_code == 200:
                bs_object = BeautifulSoup(html_object.text, "html.parser")
                img_data = bs_object.find_all("img")
                for j in enumerate(img_data[1:101]):
                    t = urlopen(j[1].attrs['src']).read()
                    forder_name = save_names[i]

                    # ========== Create directory ==========
                    try:
                        if not (os.path.isdir("images/" + forder_name)):
                            # Make the img folder
                            os.makedirs(os.path.join("images/" + forder_name))
                    except:
                        print("폴더 에러.")
                    try:
                        if not (os.path.isdir("cropImages/" + forder_name)):
                            # Make the img folder
                            os.makedirs(os.path.join("cropImages/" + forder_name))
                    except:
                        print("폴더 에러.")

                    filename = "images/" + forder_name + "/" + str(j[0] + 1) + '.jpg'
                    with open(filename, "wb+") as f:
                        f.write(t)
                print(str(star_names[i]) + " Img Save Success")


if __name__ == "__main__":
    star_crawler()