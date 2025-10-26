from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QVBoxLayout)

from instr import *
from Second_Screen import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() #Tampilan Jendela
        self.initUI() #Elemen Grafis
        self.connects() #Hubungan antar elemen
        self.show() #Start

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    #Setup Widget & Layout
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.hello_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.instruction, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.main_layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.second_win = TestWin()

app = QApplication([])
mw = MainWindow()
app.exec_()