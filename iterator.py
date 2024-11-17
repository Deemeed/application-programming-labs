import os

class Iterator:
    def __init__(self, img_dir: str):

        """
        Constructor
        :param img_dir: Directory with images
        """

        data = [os.path.join(img_dir, item) for item in os.listdir(img_dir)]
        self.data = data
        self.noOfElements = len(data)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:

        """
        Next element
        :return: element in data
        """

        if self.count < self.noOfElements:
            image = self.data[self.count]
            self.count += 1

            return image
        else:
            raise StopIteration

