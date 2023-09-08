from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QHBoxLayout, QVBoxLayout,QGroupBox,QRadioButton,QLineEdit,QLabel,
                             QPushButton,)

from instr import*

class Test2Win(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.initUi()
        self.show()

    def set_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUi(self):
        self.workh_test = QLabel(txt_workheart)
        self.index_test = QLabel(txt_index)

        self.line_Layout = QVBoxLayout()

        self.line_Layout.addWidget(self.index_test,alignment= Qt.AlignCenter)
        self.line_Layout.addWidget(self.workh_test,alignment= Qt.AlignCenter)

        self.setLayout(self.line_Layout)


def connects():
    pass