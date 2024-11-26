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

        self.file = None
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

        self.image_label.setText("Selecting file...")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getExistingDirectory(self, "Select Directory", "", options=options)
        if file:
            self.iterator = Iterator(file)
            self.next_image()
        else:
            self.show_message("File have not been opened")

    def next_image(self):

        """
        Showing next image by pushing the 'Next' button
        :return: None
        """

        if not self.iterator:
            self.show_message("Select directory first!")
            return

        try:
            image = next(self.iterator)
            pixmap = QPixmap(image)
            self.image_label.setPixmap(pixmap)
        except StopIteration:
            self.show_message("Error!")

    def show_message(self, text: str):

        """
        Warning window
        """

        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as exc:
        print(f"Something went wrong: {exc}")

