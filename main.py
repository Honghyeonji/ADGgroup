from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import random
import sys
import yut
import Nameinput
import pygame

pygame.mixer.init()

port = 2020

formGame = uic.loadUiType("practice.ui")[0]

class WindowClass(QMainWindow, formGame):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 플레이어1,2 객체 생성
        self.p1 = yut.Player()
        self.p2 = yut.Player()

        # 윷놀이판 배경
        self.background.setStyleSheet('image:url(backgroundEx.png)')

        # 플레이어 말 이미지 설정
        self.player1img = {"player1": 'image:url(player1_1.png)', "player2": 'image:url(player1_2.png)',
                           "player3": 'image:url(player1_3.png)', "player4": 'image:url(player1_4.png)',
                           "player12": 'image:url(player1_12.png)', "player13": 'image:url(player1_13.png)',
                           "player14": 'image:url(player1_14.png)', "player23": 'image:url(player1_23.png)',
                           "player24": 'image:url(player1_24.png)', "player34": 'image:url(player1_34.png)',
                           "player123": 'image:url(player1_123.png)', "player124": 'image:url(player1_124.png)',
                           "player134": 'image:url(player1_134.png)', "player234": 'image:url(player1_234.png)',
                           "player1234": 'image:url(player1_1234.png)'}
        self.player2img = {"player1": 'image:url(player2_1.png)', "player2": 'image:url(player2_2.png)',
                           "player3": 'image:url(player2_3.png)', "player4": 'image:url(player2_4.png)',
                           "player12": 'image:url(player2_12.png)', "player13": 'image:url(player2_13.png)',
                           "player14": 'image:url(player2_14.png)', "player23": 'image:url(player2_23.png)',
                           "player24": 'image:url(player2_24.png)', "player34": 'image:url(player2_34.png)',
                           "player123": 'image:url(player2_123.png)', "player124": 'image:url(player2_124.png)',
                           "player134": 'image:url(player2_134.png)', "player234": 'image:url(player2_234.png)',
                           "player1234": 'image:url(player2_1234.png)'}

        # 플레이어 말 대기 칸
        self.playerWait = [[self.player0_0Wait, self.player0_1Wait, self.player0_2Wait, self.player0_3Wait],
                           [self.player1_0Wait, self.player1_1Wait, self.player1_2Wait, self.player1_3Wait]]
        self.emptyCan = "background-color: rgba(255, 255, 255, 0);"    # 말이 놓여져있지 않은 투명한 can 적용을 위한 배경값 설정

        # 게임판
        self.cans = {'11': self.can1_1, '12': self.can1_2, '13': self.can1_3, '14': self.can1_4, '15': self.can1_5,
                     '21': self.can2_1, '22': self.can2_2, '23': self.can2_3, '24': self.can2_4, '25': self.can2_5,
                     '31': self.can3_1, '32': self.can3_2, '33': self.can3_3, '34': self.can3_4, '35': self.can3_5,
                     '41': self.can4_1, '42': self.can4_2, '43': self.can4_3, '44': self.can4_4, '45': self.can4_5,
                     '51': self.can5_1, '52': self.can5_2,
                     '61': self.can6_1, '62': self.can6_2,
                     '71': self.can7_1, '72': self.can7_2,
                     '81': self.can8_1, '82': self.can8_2,
                     '90': self.canMain}
        self.cansimage = {'11': self.emptyCan, '12': self.emptyCan, '13': self.emptyCan,
                          '14': self.emptyCan, '15': self.emptyCan, '21': self.emptyCan,
                          '22': self.emptyCan, '23': self.emptyCan, '24': self.emptyCan,
                          '25': self.emptyCan, '31': self.emptyCan, '32': self.emptyCan,
                          '33': self.emptyCan, '34': self.emptyCan, '35': self.emptyCan,
                          '41': self.emptyCan, '42': self.emptyCan, '43': self.emptyCan,
                          '44': self.emptyCan, '45': self.emptyCan, '51': self.emptyCan,
                          '52': self.emptyCan, '61': self.emptyCan, '62': self.emptyCan,
                          '71': self.emptyCan, '72': self.emptyCan, '81': self.emptyCan,
                          '82': self.emptyCan, '90': self.emptyCan}
        # 콤보박스에서 이동시킬 말 선택했을 때 이동함수에 인자로 넣어줄 값 바꿔줄 딕셔너리
        self.players = {'1번 말': 'player1', '2번 말': 'player2', '3번 말': 'player3', '4번 말': 'player4',
                        '12번 말': 'player12', '13번 말': 'player13', '14번 말': 'player14', '23번 말': 'player23',
                        '24번 말': 'player24', '34번 말': 'player34', '123번 말': 'player123', '124번 말': 'player124',
                        '134번 말': 'player134', '234번 말': 'player234', '1234번 말': 'player1234'}

        # player1 화면 기준 player2Turn일 경우 버튼비활성화
        # 이건 소켓서버클라이언트 성공하면 씁니다.
        # if(self.plyaerTurn.Text() == str(self.p2Name) + " Turn"):
        #     self.moveButton.setEnable(True)
        #     self.randomYut.setEnable(True)
        # else:
        #     self.moveButton.setDisable(True)
        #     self.randomYut.setDisable(True)

        self.moveButton.clicked.connect(self.moveButtonClicked)
        self.randomYut.clicked.connect(self.randomYutButtonClicked)

        self.turnnum = 0
        self.turn = {1: self.p1.name, 2: self.p2.name}

        self.startGame()

    # 승자가 정해지고 게임을 다시 할 때 쓰임
    def startGame(self):
        # 다시 시작시 p1, p2 리셋
        self.p1.reset()
        self.p2.reset()
        # p1, p2 닉네임 입력창
        # 일단 위의 입력칸이 플레이어1의 닉네임, 아래 입력칸이 플레이어2의 닉네임입니다. 추후에 디자인 수정하겠습니다.
        # 입력창의 기본값으로 해둔 닉네임을 입력하세요로 들어오면 player1은 쿠민이가 닉네임 기본값으로, player2는 국냥이가 닉네임 기본값으로 들어갑니다.
        inputchang = Nameinput.NameInput()
        r = inputchang.showModel()
        if r:
            self.p1.name = inputchang.inputName.text() if inputchang.inputName.text() != "닉네임을 입력하세요" and len(inputchang.inputName.text()) <= 10 else "쿠민이"
            self.player1Name.setText(self.p1.name)
            self.p2.name = inputchang.inputName_2.text() if inputchang.inputName_2.text() != "닉네임을 입력하세요" and len(inputchang.inputName.text()) <= 10 else "국냥이"
            self.player2Name.setText(self.p2.name)

        # 게임 시작 후 배경음악 재생 #Music: https://www.bensound.com
        pygame.mixer.music.load("music.wav")
        pygame.mixer.music.play(-1)

        # 플레이어 말 대기 칸
        for i in range(4):
            self.playerWait[0][i].setStyleSheet(self.player1img["player" + str(i + 1)])
        for i in range(4):
            self.playerWait[1][i].setStyleSheet(self.player2img["player" + str(i + 1)])

        # 선플레이어 정하기, 선플레이어는 랜덤
        self.turnnum = random.randrange(1, 3)
        if self.turnnum == 1: self.p1.chance += 1
        elif self.turnnum == 2: self.p2.chance += 1
        self.turn = {1: self.p1.name, 2: self.p2.name}
        self.yutResult.setText(self.turn[self.turnnum] + "님의 윷 : ")
        self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")
        self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")

        # 윷놀이판 초기화
        for key in self.cansimage.keys():
            self.cansimage[key] = self.emptyCan
        for key in self.cans.keys():
            self.cans[key].setStyleSheet(self.cansimage[key])
        print("success1")

        # 윷 던지고 말 이동하기
    def moveButtonClicked(self):
        if self.turnnum == 1:
            inputplayer = self.players[self.pNumChoose1.currentText()]
            # 현재 이동시킬 말이 이동이 가능한지 확인
            if self.usefindP(inputplayer):
                try:
                    # 말 이동, 업기, 잡기 실행
                    movedcan = self.p1.move(inputplayer)
                    print("success1-2")
                    if movedcan != "goal" and movedcan != "no":
                        self.japgi(movedcan)
                except:
                    self.playHelper.setText("오류가 생겼습니다. \n다시 이동버튼을 눌러주세요")
                    return
                print("success2")
                # 플레이어1과 플레이어2의 말들의 위치 합쳐서 윷놀이판 갱신하기
                # 1. 윷놀이판 초기화
                for key in self.cansimage.keys():
                    self.cansimage[key] = self.emptyCan
                print("success3")
                # 플레이어1 위치부터 맵에 갱신
                for key, value in self.p1.mapCan.items():
                    if value != "empty":  # 맵위에 있는 플레이어색출
                        # 맵위에 서있는 플레이어 이름의 이미지 self.player1img[key] , value - 칸좌표
                        self.cansimage[key] = self.player1img[value]
                    elif value == "empty":
                        self.cansimage[key] = self.emptyCan
                print("success4")
                # 플레이어2 위치 중 빈칸이 아닌 것들만 추가
                for key, value in self.p2.mapCan.items():
                    if value != "empty" and self.cansimage[key] == self.emptyCan:
                        self.cansimage[key] = self.player2img[value]
                print("success5")
                # 윷놀이판 갱신
                for key in self.cans.keys():
                    self.cans[key].setStyleSheet(self.cansimage[key])
                print("success6")
                # 플레이어 말이 모두 골인했을 때 종료 메시지 뜨기
                if self.p1.goalplayer == 4:
                    self.ExitGame()

                # 플레이어1의 찬스가 더이상 없으면 플레이어2로 턴 넘기기
                if self.p1.chance == 0:
                    self.turnnum = 2
                    self.p2.chance = 1
                    self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")
                    self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")
                # 있으면 플레이어2차례 유지
                else:
                    self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")
                print("success7")
            else:
                self.playHelper.setText(self.turn[self.turnnum] + "님 " + self.pNumChoose.currentText() + "은 사용이 불가합니다. \n다른 말을 골라주세요")

        elif self.turnnum == 2:
            inputplayer = self.players[self.pNumChoose2.currentText()]
            # 현재 이동시킬 말이 이동이 가능한지 확인
            if self.usefindP(inputplayer):
                try:
                    # 말 이동, 업기, 잡기 실행
                    movedcan = self.p2.move(inputplayer)
                    print("success1-2")
                    if movedcan != "goal" and movedcan != "no":
                        self.japgi(movedcan)
                except:
                    self.playHelper.setText("오류가 생겼습니다. \n다시 이동버튼을 눌러주세요")
                    return
                print("success2")
                # 플레이어1과 플레이어2의 말들의 위치 합쳐서 윷놀이판 갱신하기
                # 1. 윷놀이판 초기화
                for key in self.cansimage.keys():
                    self.cansimage[key] = self.emptyCan
                print("success3")
                # 플레이어1 위치부터 맵에 갱신
                for key, value in self.p1.mapCan.items():
                    if value != "empty":  # 맵위에 있는 플레이어색출
                        # 맵위에 서있는 플레이어 이름의 이미지 self.player1img[key] , value - 칸좌표
                        self.cansimage[key] = self.player1img[value]
                    elif value == "empty":
                        self.cansimage[key] = self.emptyCan
                print("success4")
                # 플레이어2 위치 중 빈칸이 아닌 것들만 추가
                # 플레이해보니 플레이어2의 말이 골인했을 때 여기서 막힘
                for key, value in self.p2.mapCan.items():
                    if value != "empty" and self.cansimage[key] == self.emptyCan:
                        self.cansimage[key] = self.player2img[value]
                print("success5")
                # 윷놀이판 갱신
                for key in self.cans.keys():
                    self.cans[key].setStyleSheet(self.cansimage[key])
                print("success6")
                # 플레이어 말이 모두 골인했을 때 종료 메시지 뜨기
                if self.p2.goalplayer == 4:
                    self.ExitGame()

                # 플레이어2의 찬스가 더이상 없으면 플레이어1로 턴 넘기기
                if self.p2.chance == 0:
                    self.turnnum = 1
                    self.p1.chance = 1
                    self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")
                    self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")
                # 있으면 플레이어2차례 유지
                else:
                    self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")
                print("success7")
            else:
                self.playHelper.setText(self.turn[self.turnnum] + "님 " + self.pNumChoose.currentText() + "은 사용이 불가합니다. \n다른 말을 골라주세요")

    # 윷던지기 함수
    def randomYutButtonClicked(self):
        # 낙일경우 이동 x 바로 턴 체인지
        # 플레이어1의 턴일 경우
        if self.turnnum == 1:
            if self.p1.chance >= 1:
                self.p1.throw()
                self.yutResult.setText(self.p1.name + "님의 윷 : " + self.p1.resultYut)
                # 낙일경우
                if self.p1.pYut == 0:
                    # 찬스가 더이상 없으면 상대방한테 턴 넘김
                    if self.p1.chance == 0:
                        self.turnnum = 2
                        self.p2.chance = 1
                    self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")
                    self.playHelper.setText(self.turn[self.turnnum]+"님 윷을 던져주세요.")
                # 낙이 아닐 경우
                else:
                    self.playHelper.setText(self.turn[self.turnnum]+"님 말을 이동시켜주세요")
        # 플레이어2의 턴일 경우
        elif self.turnnum == 2:
            if self.p2.chance >= 1:
                self.p2.throw()
                self.yutResult.setText(self.p2.name + "님의 윷 : " + self.p2.resultYut)
                if self.p2.pYut == 0:
                    if self.p2.chance == 0:
                        self.turnnum = 1
                        self.p1.chance = 1
                    self.playerTurn.setText("현재 차례: " + self.turn[self.turnnum] + "님")
                    self.playHelper.setText(self.turn[self.turnnum] + "님 윷을 던져주세요.")
                else:
                    self.playHelper.setText(self.turn[self.turnnum] + "님 말을 이동시켜주세요")
        print("successrandom")

    # 승자 정해졌을 때 나오는 창
    def ExitGame(self):
        result = QMessageBox.information(self
                                         , "게임종료"
                                         , self.turn[self.turnnum]+"님 승리! \n다시시작 : Yes, 종료 : No"
                                         , QMessageBox.Ok | QMessageBox.No)
        if result == QMessageBox.Ok:
            self.startGame()
        else:
            self.close()

    def japgi(self, nowLocation):
        # 플레이어1의 턴일 경우 플레이어2의 로케이션과 플레이어1 로케이션이 겹치지는지 확인 후 겹치면 플레이어2 해당 로케이션을 초기화
        if self.turnnum == 1:
            for key, value in self.p2.playerLocation.items():
                if nowLocation == value:
                    self.p2.playerLocation[key] = "noLocation"
                    self.p1.chance = self.p1.chance + 1
                    for k, v in self.p2.mapCan.items():
                        if key == v:
                            self.p2.mapCan[k] = "empty"
                    print("j1")
                    # usable, unusable 갱신
                    self.p2.unusable.append(key)
                    self.p2.usable.remove(key)
                    for a in range(1, 5):
                        print("j2")
                        if key.find(str(a)) != -1:
                            print("j3")
                            try:
                                self.p2.unusable.remove("player" + str(a))
                                self.p2.usable.append("player" + str(a))
                            except:
                                continue
                    self.p2.usable = list(set(self.p2.usable))
                    self.p2.unusable = list(set(self.p2.unusable))
                    print("j7")
        # 플레이어2의 턴일 경우 플레이어1의 로케이션과 플레이어2 로케이션이 겹치지는지 확인 후 겹치면 플레이어1 해당 로케이션을 초기화
        elif self.turnnum == 2:
            for key, value in self.p1.playerLocation.items():
                if nowLocation == value:
                    self.p1.playerLocation[key] = "noLocation"
                    self.p2.chance = self.p2.chance + 1
                    for k, v in self.p1.mapCan.items():
                        if key == v:
                            self.p1.mapCan[k] = "empty"
                    print("j1")
                    # usable, unusable 갱신
                    self.p1.unusable.append(key)
                    self.p1.usable.remove(key)
                    for a in range(1, 5):
                        print("j2")
                        if key.find(str(a)) != -1:
                            print("j3")
                            try:
                                self.p1.unusable.remove("player" + str(a))
                                self.p1.usable.append("player" + str(a))
                            except: continue
                    self.p1.usable = list(set(self.p1.usable))
                    self.p1.unusable = list(set(self.p1.unusable))
                    print("j7")

    def usefindP(self, inputplayer):
        if self.turnnum == 1:
            for i in self.p1.usable:
                if inputplayer == i:
                    return True
        if self.turnnum == 2:
            for i in self.p2.usable:
                if inputplayer == i:
                    return True
        return False



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()