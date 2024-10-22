import csv
import os
from msilib.text import dirname


def make_annotation(annotation_file: str, img_dir: str) -> None:

    """
    Making annotation which contains the absolute and relative path to each image
    :param annotation_file: Path to file to save annotation
    :param img_dir: Directory with images
    :return: None
    """

    data = []
    for filename in os.listdir(img_dir):
        relative_filepath = os.path.join(img_dir, filename)
        absolute_filepath = os.path.abspath(relative_filepath)
        data.append([relative_filepath, absolute_filepath])

    if os.path.exists(annotation_file):
        os.remove(annotation_file)

    with open(annotation_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

