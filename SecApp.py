from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Quiz Singkat Saja ╰(*°▽°*)╯")
main_window.resize(500, 200)

lbl_question = QLabel("Wewok detok, not onli...")

rbtn_answer1 = QRadioButton("tok detok")
rbtn_answer2 = QRadioButton("talk to talk")
rbtn_answer3 = QRadioButton("tototok")
rbtn_answer4 = QRadioButton("19 juta lapangan basket")

layout_row1 = QHBoxLayout()
layout_row1.addWidget(rbtn_answer1, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row1.addWidget(rbtn_answer2, alignment = Qt.AlignmentFlag.AlignCenter)

layout_row2 = QHBoxLayout()
layout_row2.addWidget(rbtn_answer3, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row2.addWidget(rbtn_answer4, alignment = Qt.AlignmentFlag.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addWidget(lbl_question, alignment = Qt.AlignmentFlag.AlignCenter)
layout_main.addLayout(layout_row1)
layout_main.addLayout(layout_row2)

#Button Functionality
def answer_true():
    victory_win = QMessageBox()
    victory_win.setText("Hidup Jok-")
    victory_win.exec_()

def answer_false():
    lose_win = QMessageBox()
    lose_win.setText("Maaf anda kurang teliti")
    lose_win.exec_()

rbtn_answer1.clicked.connect(answer_true)
rbtn_answer2.clicked.connect(answer_false)
rbtn_answer3.clicked.connect(answer_false)
rbtn_answer4.clicked.connect(answer_false)

main_window.setLayout(layout_main)
main_window.show()
app.exec_()