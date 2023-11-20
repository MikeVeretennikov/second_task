import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False


    def run(self):
        self.do_paint = True
        self.pushButton.hide()
        self.update()


    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()
        self.do_paint = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(238, 210, 2))

        for i in range(10):
            a = random.randint(20, 400)
            coord1 = random.randint(0, 1000)
            coord2= random.randint(1,1000)
            qp.drawEllipse(coord1, coord2, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
