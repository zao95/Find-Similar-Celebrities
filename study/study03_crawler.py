import os
import requests as re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def input_data(rank, title, artist):
    return {"rank": rank, "title": title, "artist": artist}


# ========== Main part ==========
if __name__ == "__main__":
    source = re.get("https://www.melon.com/chart/index.htm", headers={"User-Agent": "XY"})
    html = BeautifulSoup(source.text, "html.parser")
    target = html.select_one("div.service_list_song")
    target_song_rank = target.select("div.t_center")
    target_song_info = target.select("div.wrap_song_info")
    count = 1
    print_list = []

    for i in target_song_info:
        try:
            target_song_info_1 = i.select_one("div.rank01")
            target_song_info_1_ = target_song_info_1.select_one("a")
            target_song_info_2 = i.select_one("span.checkEllipsis")
            target_song_info_2_ = target_song_info_2.select_one("a")
            print_list.append(
                input_data(
                    count,
                    target_song_info_1_.text.strip().replace("/", "-").replace("\"", "'").replace(":", "_"),
                    target_song_info_2_.text.strip().replace("/", "-").replace("\"", "'").replace(":", "_")
                )
            )
        except:
            continue
        count += 1

    for song in print_list:
        url_info = "https://www.google.co.kr/search?"
        params = {
            "q": song["title"] + " " + song["artist"],
            "tbm": "isch"
        }
        # url 요청 파싱값
        html_object = re.get(url_info, params)
        if html_object.status_code == 200:
            bs_object = BeautifulSoup(html_object.text, "html.parser")
            img_data = bs_object.find_all("img")
            for i in enumerate(img_data[1:11]):
                t = urlopen(i[1].attrs['src']).read()
                forder_name = song["title"] + "_" + song["artist"]

                # ========== Create directory ==========
                # If not the img folder
                temp_folder_name = "t"
                try:
                    if not (os.path.isdir("images/" + forder_name)):
                        # Make the img folder
                        os.makedirs(os.path.join("images/" + forder_name))
                except:
                    print("폴더 에러.")

                filename = "images/" + forder_name + "/" + str(i[0] + 1) + '.jpg'
                with open(filename, "wb+") as f:
                    f.write(t)
            print(str(song["rank"]) + " Img Save Success")