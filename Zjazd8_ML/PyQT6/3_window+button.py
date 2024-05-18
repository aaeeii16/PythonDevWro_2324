from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja aplikacja')
        self.setFixedSize(600, 400)
        self.button = QPushButton('Przycisk')
        self.button.pressed.connect(self.button_pressed)
        self.setCentralWidget(self.button)

    def button_pressed(self):
        print('wcisniety')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()