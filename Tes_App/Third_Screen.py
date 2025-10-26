from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QVBoxLayout,
    QMessageBox, QRadioButton, QHBoxLayout)
from PyQt5.QtGui import (QFont)

from instr import *

class FinalWindow(QWidget):
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
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, allignment=Qt.AllignCenter)
        self.layout_line.addWidget(self.workh_text, allignment=Qt.AllignCenter)
        self.setLayout(self.layout_line)