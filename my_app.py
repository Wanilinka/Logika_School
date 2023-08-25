from PyQt5.Core import Qt 
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QHBoxLayout, QVBoxLayout,QGroupBox,QRadioButton,QLineEdit)

from instr import*

class MainWin (QWidget):
    def set_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        pass
    def connects(self):
        pass