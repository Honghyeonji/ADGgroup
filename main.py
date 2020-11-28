from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtGui import *
from PyQt5 import uic
import random
import sys
import yut
import Nameinput
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.wav")  #Music: https://www.bensound.com #음원 바꾸셔도 괜찮습니다 같은 폴더에 음악파일 필요합니다.
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

        # 게임판
        self.cans = { '00':self.can0_0, '01':self.can0_1, '02':self.can0_2, '03':self.can0_3, '04':self.can0_4,
                      '10':self.can1_0, '11':self.can1_1, '12':self.can1_2, '13':self.can1_3, '14':self.can1_4,
                      '20':self.can2_0, '21':self.can2_1, '22':self.can2_2, '23':self.can2_3, '24':self.can2_4,
                      '30':self.can3_0, '31':self.can3_1, '32':self.can3_2, '33':self.can3_3, '34':self.can3_4,
                      '40':self.can4_0, '41':self.can4_1,
                      '50':self.can5_0, '51':self.can5_1,
                      '60':self.can6_0, '61':self.can6_1,
                      '70':self.can7_0, '71':self.can7_1, }

        # self.cansWH = { '00': "empty", '01': "empty", '02': "empty", '03': "empty", '04': "empty",
        #                 '10': "empty", '11': "empty", '12': "empty", '13': "empty", '14': "empty",
        #                 '20': "empty", '21': "empty", '22': "empty", '23': "empty", '24': "empty",
        #                 '30': "empty", '31': "empty", '32': "empty", '33': "empty", '34': "empty",
        #                 '40': "empty", '41': "empty",
        #                 '50': "empty", '51': "empty",
        #                 '60': "empty", '61': "empty",
        #                 '70': "empty", '71': "empty", }

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

        self.turnnum = 0
        self.turn = {1:self.p1.name, 2:self.p2.name}

        self.startGame() # 승자가 정해지고 게임을 다시 할 때 쓰임

    def startGame(self):
        # p1, p2 닉네임 입력창
        # 일단 위의 입력칸이 플레이어1의 닉네임, 아래 입력칸이 플레이어2의 닉네임입니다. 추후에 디자인 수정하겠습니다.
        # 입력창의 기본값으로 해둔 닉네임을 입력하세요로 들어오면 player1은 쿠민이가 닉네임 기본값으로, player2는 국냥이가 닉네임 기본값으로 들어갑니다.
        inputchang = Nameinput.NameInput()
        r = inputchang.showModel()
        if r:
            self.p1.name = inputchang.inputName.text() if inputchang.inputName.text() != "닉네임을 입력하세요" else "쿠민이"
            self.player1Name.setText(self.p1.name)
            self.p2.name = inputchang.inputName_2.text() if inputchang.inputName_2.text() != "닉네임을 입력하세요" else "국냥이"
            self.player2Name.setText(self.p2.name)

        # 플레이어 말 대기 칸
        for i in range(4):
            self.playerWait[0][i].setStyleSheet(self.player1img[i + 1])
        for i in range(4):
            self.playerWait[1][i].setStyleSheet(self.player2img[i + 1])

        self.turnnum = random.randrange(1, 3)  # 선플레이어는 랜덤
        self.turn = {1: self.p1.name, 2: self.p2.name}
        self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")

        self.canMain.setStyleSheet(self.emptyCan)
        for key, vaule in self.cans.items():
            self.cans[key].setStyleSheet(self.emptyCan)


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