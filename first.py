import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.draw_circle)

        self.circles = []

    def draw_circle(self):
        diameter = random.randint(20, 100)
        self.circles.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))

        for diameter in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())