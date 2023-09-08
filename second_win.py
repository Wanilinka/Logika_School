from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,QWidget,
                             QHBoxLayout, QVBoxLayout,QGroupBox,QRadioButton,QLineEdit,QLabel,
                             QPushButton,)

from instr import*
from final_win import*

class TestWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUi(self):
        self.text_timer = txt_timer
        self.text_name = txt_name
        self.line_name = txt_hintname
        self.text_age = txt_age
        self.line_age = txt_hintage
        self.text_test1 = txt_test1
        self.btn_test1 = txt_starttest1
        self.line_test = txt_hinttest1
        self.text_test2 = txt_test2
        self.btn_test2 = txt_starttest2
        self.text_test3 = txt_test3
        self.btn_test3 = txt_starttest3
        self.line_test2 = txt_hinttest2
        self.line_test3 = txt_hinttest3
        self.btn_next = txt_sendresults

        self.l_line = QHBoxLayout()
        self.r_line = QHBoxLayout()
        self.h_line = QHBoxLayout()
        
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignLeft)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def timer_test(self):
        global time
        time = QTime(0,0,16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer_sits(self):
        global time
        time = QTime(0,0,31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer_final(self):
        global time
        time = QTime(0,1,1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)


    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color:rgb(0,255,0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color:rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color:rgb(0,255,0)")

        if time.toString("hh:mm:ss") <=45:
            self.text_timer.setStyleSheet("color:rgb(0,0,0)")

        if time.toString("hh:mm:ss") <=15:
            self.text_timer.setStyleSheet("color:rgb(0,255,0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)

    def next_click(self):
        self.fw=Test2Win()
        self.hide()
    
