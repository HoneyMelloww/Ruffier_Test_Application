from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Gacha (╹ڡ╹ )")
main_window.resize(400, 200)

lbl_title = QLabel("Click tombol untuk Gacha")
lbl_result = QLabel("(～￣▽￣)～")
btn_generate = QPushButton("Gacha!")
btn_generate10 = QPushButton("Gacha 10 Pull!")

layout_main = QVBoxLayout()
layout_main.addWidget(lbl_title, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(lbl_result, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(btn_generate, alignment=Qt.AlignmentFlag.AlignCenter)
layout_main.addWidget(btn_generate10, alignment=Qt.AlignmentFlag.AlignCenter)

def get_rarity():
    number = randint(1, 1000)
    if number <= 5:
        return "SSR"
    elif number <= 35:
        return "SR"
    elif number <= 100:
        return "S"
    elif number <= 200:
        return "A"
    elif number <= 550:
        return "B"
    else:
        return "C"

def random_number():
    result = get_rarity()
    lbl_result.setText(result)
    return result

def ten_pull(random_number):
    results = {"SSR": 0, "SR": 0, "S": 0, "A": 0, "B": 0, "C": 0}

    draws = []
    for _ in range(10):
        r = get_rarity()
        results[r] += 1
        draws.append(r)

    summary = " | ".join(f"{r}[{n}]" for r, n in results.items())
    lbl_result.setText(summary)

btn_generate.clicked.connect(random_number)
btn_generate10.clicked.connect(ten_pull)

main_window.setLayout(layout_main)
main_window.show()

app.exec_()