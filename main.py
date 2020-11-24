from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtGui import *
from PyQt5 import uic
import sys

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("practice.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 윷놀이판 배경
        self.background.setStyleSheet('image:url(backgroundEx.png)')
        # 플레이어 말 이미지 설정
        self.player = [['image:url(player1_1.png)', 'image:url(player1_2.png)', 'image:url(player1_3.png)', 'image:url(player1_4.png)'],
                  ['image:url(player2_1.png)', 'image:url(player2_2.png)', 'image:url(player2_3.png)', 'image:url(player2_4.png)']]
        # 플레이어 말 대기 칸
        self.playerWait = [[self.player0_0Wait, self.player0_1Wait, self.player0_2Wait, self.player0_3Wait],
                      [self.player1_0Wait, self.player1_1Wait, self.player1_2Wait, self.player1_3Wait]]
        self.emptyCan = "background-color: rgba(255, 255, 255, 0);"    # 말이 놓여져있지 않은 투명한 can 적용을 위한 배경값 설정

        for i in range(2):
            for j in range(4):
                self.playerWait[i][j].setStyleSheet(self.player[i][j])

        # 윷놀이 판 칸 설정
        self.cans = [[self.can0_0, self.can0_1, self.can0_2, self.can0_3, self.can0_4],  # [0:3] 모서리 줄
                      [self.can1_0, self.can1_1, self.can1_2, self.can1_3, self.can1_4],
                      [self.can2_0, self.can2_1, self.can2_2, self.can2_3, self.can2_4],
                      [self.can3_0, self.can3_1, self.can3_2, self.can3_3, self.can3_4],
                      [self.can4_0, self.can4_1],   # [4:7] 가운데 줄
                      [self.can5_0, self.can5_1],
                      [self.can6_0, self.can6_1],
                      [self.can7_0, self.can7_1]]

        self.canMain.setStyleSheet(self.emptyCan)
        for i in range(4):
            for j in range(5):
                self.cans[i][j].setStyleSheet(self.emptyCan)
            for j in range(2):
                self.cans[i+4][j].setStyleSheet(self.emptyCan)




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()