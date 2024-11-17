import os.path
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QVBoxLayout, QWidget
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
        
        img_dir, ok = QInputDialog.getText(self, "Selecting file", "Enter path to file: ")
        if ok & os.path.exists(img_dir):
            self.iterator = Iterator(img_dir)
            self.next_image()
        else:
            self.image_label.setText("Please try other path")

    def next_image(self):

        """
        Showing next image py pushing the 'Next' button
        :return: None
        """
        
        if not self.iterator:
            self.image_label.setText("Firstly select a file to read!")
            return

        image = self.iterator.__next__()
        if image:
            pixmap = QPixmap(image)
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("No images left!")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as exc:
        print(f"Something went wrong: {exc}")

