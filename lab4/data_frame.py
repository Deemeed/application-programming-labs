import cv2
import matplotlib.pyplot as plt
import pandas as pd


def make_df(file: str) -> pd.DataFrame:

    """
    Making DataFrame from csv file
    :param file: Annotation file
    :return: DataFrame
    """

    df = pd.read_csv(file, names = ['RelPath', 'AbsPath'])

    return df

def add_dimensions(df: pd.DataFrame) -> None:

    """
    Adding columns with dimensions of images
    :param df: DataFrame
    :return: None
    """

    images = [cv2.imread(img) for img in df['AbsPath']]

    df['Height'] = [img.shape[0] for img in images]
    df['Width'] = [img.shape[1] for img in images]
    df['Channels'] = [img.shape[2] for img in images]

def get_statistics(df: pd.DataFrame) -> None:

    """
    Printing statistics for Height, Width and Channels columns
    :param df: DataFrame
    :return: None
    """

    print(df[['Height', 'Width', 'Channels']].describe())

def sort_df(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:

    """
    Sorting df with conditions: height < max_height, width < max_width
    :param df: DataFrame
    :param max_height: Max height
    :param max_width: Max width
    :return: Sorted DataFrame
    """

    sdf = df.copy(deep=True)[(df["Height"] < max_height) & (df["Width"] < max_width)]

    return sdf

def add_area(df: pd.DataFrame) -> None:

    """
    Adding Area column to df
    :param df: DataFrame
    :return: None
    """

    df['Area'] = (df['Height'] * df['Width'])

def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:

    """
    Sorting df by Area column
    :param df: DataFrame
    :return: Sorted DataFrame
    """

    sdf = df.sort_values(by = 'Area')

    return sdf

def histogram(df: pd.DataFrame) -> None:

    """
    Showing histogram by Area column
    :param df: DataFrame
    :return: None
    """

    plt.figure()

    df['Area'].diff().hist()

    plt.title('Histogram')
    plt.xlabel('Area')
    plt.ylabel('Count')

    plt.show()

