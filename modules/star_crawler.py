import os
from icrawler.builtin import GoogleImageCrawler


def star_crawler(star_names):
    count = 0
    for i in star_names:
        folder_name = count
        try:
            if not (os.path.isdir("images/" + str(folder_name))):
                os.makedirs(os.path.join("images/" + str(folder_name)))
        except Exception as e:
            print("폴더 에러.")
            print(e)
        try:
            if not (os.path.isdir("cropImages/" + str(folder_name))):
                os.makedirs(os.path.join("cropImages/" + str(folder_name)))
        except Exception as e:
            print("폴더 에러.")
            print(e)

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=6,
            downloader_threads=12,
            storage={'root_dir': "images/" + str(folder_name)}
        )
        filters = dict(
            size='large'
        )
        google_crawler.crawl(keyword=i, filters=filters, max_num=100, file_idx_offset=0)
        count += 1


if __name__ == "__main__":
    star_crawler()
