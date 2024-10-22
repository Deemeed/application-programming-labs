import argparse
from download import download_images
from annotation import make_annotation
from iterator import Iterator


def parse_args() -> tuple[str, str, str]:

    """
    Parsing arguments from cmd
    :return: tuple of parsed arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='keyword to search')
    parser.add_argument('-d', '--img_dir', type=str, help='directory to save')
    parser.add_argument('-f', '--annotation_file', type=str, help='file to annotation')

    args = parser.parse_args()

    return args.keyword, args.img_dir, args.annotation_file


def main():
    keyword, img_dir, annotation_file = parse_args()
    try:
        download_images(keyword, img_dir)
        make_annotation(annotation_file, img_dir)

        iterator = Iterator(img_dir)
        for item in iterator:
            print(item)

    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == "__main__":
    main()

