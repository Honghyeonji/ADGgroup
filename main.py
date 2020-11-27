from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
# import socket
# import server
import yut
from NameInput import NameInput

port = 2020

formGame = uic.loadUiType("practice.ui")[0]

class WindowClass(QMainWindow, formGame) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # self.s = server.ServerSocket(self)
        # self.ip = socket.gethostbyname(socket.gethostname())
 
        # 닉네임 입력창
        inputchang = NameInput()
        r = inputchang.showModel()
        if r:
            self.p2Name = inputchang.inputName.text()
            self.player2Name.setText(self.p2Name)

        # 윷놀이판 배경
        self.background.setStyleSheet('image:url(backgroundEx.png)')
        # 플레이어 말 이미지 설정

        self.player1img = {1: 'image:url(player1_1.png)', 2: 'image:url(player1_2.png)', 3: 'image:url(player1_3.png)', 4: 'image:url(player1_4.png)',
                           12: 'image:url(player1_12.png)', 13: 'image:url(player1_13.png)', 14: 'image:url(player1_14.png)',
                           23: 'image:url(player1_23.png)', 24: 'image:url(player1_24.png)',
                           123: 'image:url(player1_123.png)', 124: 'image:url(player1_124.png)',
                           234: 'image:url(player1_234.png)', 1234: 'image:url(player1_1234.png)'}
        self.player2img = {1: 'image:url(player2_1.png)', 2: 'image:url(player2_2.png)', 3: 'image:url(player2_3.png)', 4: 'image:url(player2_4.png)',
                           12: 'image:url(player2_12.png)', 13: 'image:url(player2_13.png)', 14: 'image:url(player2_14.png)',
                           23: 'image:url(player2_23.png)', 24: 'image:url(player2_24.png)',
                           123: 'image:url(player2_123.png)', 124: 'image:url(player2_124.png)',
                           234: 'image:url(player2_234.png)', 1234: 'image:url(player2_1234.png)'}

        # 플레이어 말 대기 칸
        self.playerWait = [[self.player0_0Wait, self.player0_1Wait, self.player0_2Wait, self.player0_3Wait],
                      [self.player1_0Wait, self.player1_1Wait, self.player1_2Wait, self.player1_3Wait]]
        self.emptyCan = "background-color: rgba(255, 255, 255, 0);"    # 말이 놓여져있지 않은 투명한 can 적용을 위한 배경값 설정

        for i in range(4):
            self.playerwait[0][i].setStyleSheet(self.player1img[i+1])
        for i in range(4):
            self.playerWait[1][i].setStyleSheet(self.player2img[i+1])

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

        # player1 화면 기준 player2Turn일 경우 버튼비활성화
        if(self.plyaerTurn.Text() == str(self.p2Name) + " Turn"):
            self.moveButton.setEnable(True)
            self.randomYut.setEnable(True)
        else:
            self.moveButton.setDisable(True)
            self.randomYut.setDisable(True)

        self.moveButton.clicked.connect(self.MoveButtonClicked)
        self.randomYut.clicked.connect(self.RandomYutButtonClicked)


            # 윷 던지고 말 이동하기
    def MoveButtonClicked(self):
        pass



    def RandomYutButtonClicked(self):
        #윷 던지는 함수
        yr = yut.throw()
        self.yutResult.setText(str(yr))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
