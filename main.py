from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
import yut
import Nameinput
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.wav") #Music: https://www.bensound.com #음원 바꾸셔도 괜찮습니다 같은 폴더에 음악파일 필요합니다.
pygame.mixer.music.play(-1)


port = 2020

formGame = uic.loadUiType("practice.ui")[0]

class WindowClass(QMainWindow, formGame) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 플레이어1,2 객체 생성
        self.p1 = yut.Player()
        self.p2 = yut.Player()

        # p1, p2 닉네임 입력창
        # 일단 위의 입력칸이 플레이어1의 닉네임, 아래 입력칸이 플레이어2의 닉네임입니다. 추후에 디자인 수정하겠습니다.
        inputchang = Nameinput.NameInput()
        r = inputchang.showModel()
        if r:
            self.p1.name = inputchang.inputName.text()
            self.player1Name.setText(self.p1.name)
            self.p2.name = inputchang.inputName_2.text()
            self.player2Name.setText(self.p2.name)

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
            self.playerWait[0][i].setStyleSheet(self.player1img[i+1])
        for i in range(4):
            self.playerWait[1][i].setStyleSheet(self.player2img[i+1])

        # 윷놀이 판 칸 설정
        # self.cans = [[self.can0_0, self.can0_1, self.can0_2, self.can0_3, self.can0_4],  # [0:3] 모서리 줄
        #               [self.can1_0, self.can1_1, self.can1_2, self.can1_3, self.can1_4],
        #               [self.can2_0, self.can2_1, self.can2_2, self.can2_3, self.can2_4],
        #               [self.can3_0, self.can3_1, self.can3_2, self.can3_3, self.can3_4],
        #               [self.can4_0, self.can4_1],   # [4:7] 가운데 줄
        #               [self.can5_0, self.can5_1],
        #               [self.can6_0, self.can6_1],
        #               [self.can7_0, self.can7_1]]

        self.cans = { '00':self.can0_0, '01':self.can0_1, '02':self.can0_2, '03':self.can0_3, '04':self.can0_4,
                      '10':self.can1_0, '11':self.can1_1, '12':self.can1_2, '13':self.can1_3, '14':self.can1_4,
                      '20':self.can2_0, '21':self.can2_1, '22':self.can2_2, '23':self.can2_3, '24':self.can2_4,
                      '30':self.can3_0, '31':self.can3_1, '32':self.can3_2, '33':self.can3_3, '34':self.can3_4,
                      '40':self.can4_0, '41':self.can4_1,
                      '50':self.can5_0, '51':self.can5_1,
                      '60':self.can6_0, '61':self.can6_1,
                      '70':self.can7_0, '71':self.can7_1, }
        self.canMain.setStyleSheet(self.emptyCan)
        for key, vaule in self.cans.items():
            self.cans[key].setStyleSheet(self.emptyCan)

        # for i in range(4):
        #     for j in range(5):
        #         self.cans[i][j].setStyleSheet(self.emptyCan)
        #     for j in range(2):
        #         self.cans[i+4][j].setStyleSheet(self.emptyCan)

        # player1 화면 기준 player2Turn일 경우 버튼비활성화
        # 이건 소켓서버클라이언트 성공하면 씁니다.
        # if(self.plyaerTurn.Text() == str(self.p2Name) + " Turn"):
        #     self.moveButton.setEnable(True)
        #     self.randomYut.setEnable(True)
        # else:
        #     self.moveButton.setDisable(True)
        #     self.randomYut.setDisable(True)

        self.moveButton.clicked.connect(self.MoveButtonClicked)
        self.randomYut.clicked.connect(self.RandomYutButtonClicked)

        self.turn = 1
        self.playerTurn.setText("현재 차례: " + str(self.turn))

            # 윷 던지고 말 이동하기
    def MoveButtonClicked(self):
        # 가정으로 만든 코드이고 오류 유발해서 주석처리 해놨습니다.
        # if(self.yutResult.text() != "윷 결과: "):
        #     if(self.turn == 1):
        #         i, j, road = p1.(윷이동하는 함수)(self.pNumChoose.text(), self.resultyut)
        #         self.cans[i].setStyleSheet(self.emptyCan)
        #         if(int(j) != -1): self.cans[j].setStyleSheet(road)
        #         # 이건 그냥 제가 가정해서 만들어본겁니다. 만약 다 dic형식으로 한다면 i는 말이 떠난 칸의 위치, j는 말이 있는 위치, road는 말의 이미지경로
        #         # 이 함수 안에서 말의 번호에 따라 다르게 인자를 넣고 다르게 리턴값을 받는다는 가정입니다!
        #         # turn을 바꾸는 판정도 정해야합니다~!
        #     if(self.turn == 2):
        #
        # self.yutResult.setText("윷 결과: ")
        pass



    def RandomYutButtonClicked(self):
        # 윷 던지는 함수
        # 오류 유발로 주석처리 해놨습니다.
        # if(self.turn == 1):
        #     self.p1.throw()
        #     self.yutResult.setText("윷 결과: " + self.p1.resultyut)
        # elif(self.turn == 2):
        #     self.p1.throw()
        #     self.yutResult.setText("윷 결과: " + self.p2.resultyut)
        pass



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()