import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, \
    QFileDialog, QMessageBox
from iterator import Iterator


class MainWindow(QMainWindow):
    def __init__(self):

        """
        Constructor of main window
        """

        super().__init__()

        self.iterator = None
        self.setWindowTitle("LAB5 DATASET VIEWER")
        self.setFixedSize(1200, 900)

        self.image_label = QLabel("No images yet", self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.next_button = QPushButton("Next image", self)
        self.next_button.clicked.connect(self.next_image)

        self.imgdir_button = QPushButton("Select file to see", self)
        self.imgdir_button.clicked.connect(self.select_file)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.imgdir_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_file(self):

        """
        Open dialog window by pushing the 'Select' button to get file path
        :return: None
        """

        file = QFileDialog.getExistingDirectory(self, "Selecting file", "C:/Users/user/PycharmProjects/lab5")
        self.iterator = Iterator(file)
        self.next_image()

    def next_image(self):

        """
        Showing next image by pushing the 'Next' button
        :return: None
        """

        if not self.iterator:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Wrong directory selected")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)

            msg_box.exec_()
            return

        image = next(self.iterator)
        if image:
            pixmap = QPixmap(image)
            self.image_label.setPixmap(pixmap)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("No images left!")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)

            msg_box.exec_()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as exc:
        print(f"Something went wrong: {exc}")

