import argparse
from data_frame import *


def parse_args() -> str:

    """
    Parse args from cmd
    :return: Name of annotation file
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='annotation file name')
    args = parser.parse_args()

    return args.filename

def main() -> None:
    try:
        file = parse_args()

        df = make_df(file)
        print(df)
        print()

        add_dimensions(df)
        print(df)
        print()

        get_statistics(df)
        print()

        sdf = sort_df(df, 1500, 1500)
        print(sdf)
        print()

        add_area(df)
        print(df)
        print()

        sdf = sort_by_area(df)
        print(sdf)

        histogram(sdf)

    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == '__main__':
    main()

