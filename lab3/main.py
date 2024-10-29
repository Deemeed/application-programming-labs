import argparse

from process_img import *


def parse_arguments() -> tuple[str, str]:

    """
    Parse arguments from cmd
    :return:Tuple of parsed arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('img', type=str, help='path to image')
    parser.add_argument('-f', '--file', type=str, help='file to save image')
    args = parser.parse_args()

    return args.img, args.file

def main():
    img, file = parse_arguments()

    try:
        image = read_image(img)
        print_size(image)
        create_histogram(image)
        binary_image = make_binary(img)
        print_difference(image, binary_image)
        save_image(file, binary_image)
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == '__main__':
    main()

