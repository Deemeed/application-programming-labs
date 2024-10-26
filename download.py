import os
import shutil
from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, img_dir: str) -> None:

    """
    Download images with keyword using GoogleImageCrawler
    :param keyword: Keyword to search images
    :param img_dir: Directory to save images
    :return: None
    """

    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)
        os.mkdir(img_dir)
    else:
        os.mkdir(img_dir)

    google_crawler = GoogleImageCrawler(
        storage={'root_dir': img_dir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4)
    google_crawler.crawl(keyword=keyword, max_num=100)

