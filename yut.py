import random
# 난수 발생을 위해 random 라이브러리 사용
'''
플레이어 이름, 플레이어 결과, 플레이어 이동, 
찬스는 여기서 생성, 말을 잡거나 모, 윷이 나왔을 때 기회 1번 추가
말 이동 시 딕셔너리 형태로 하는 것을 가정 {yutArrayNum : player 이미지}
말이 이동했을 때 이동하는 인덱스
'''


class Player:
    def __init__(self):

        # 이동 함수에서만 쓰일 pYut = 0  # 사용자의 도,개,걸,윷,모,빽도,낙의 이동해야할 칸수를 저장합니다.
        # -> 이동함수 인자로 이동시킬 플레이어말넘버와 윷 결과를 넣고
        # -> 아래의 self.yuts 딕으로 이동시킬 칸을 찾아 pYut에 넣고 그 값에 따라 이동하게
        self.yutrandoms = []  # 확률 구성 리스트
        self.yuts = {"빽도":-1, "낙":0, "도":1, "개":2, "걸":3, "윷":4, "모":5}
        self.name = '' # 플레이어 닉네임
        self.resultyut = ''
        # 플레이어
        self.player1_1 = [0][0]
        self.player1_2 = [0][0]
        self.player1_3 = [0][0]
        self.player1_4 = [0][0]

        self.player2_1 = [0][0]
        self.player2_2 = [0][0]
        self.player2_3 = [0][0]
        self.player2_4 = [0][0]

        #윷놀이판 배열
        # self.yutArray = [[0][0], [0][1], [0][2], [0][3], [0][4],
        #                  [1][0], [1][1], [1][2], [1][3], [1][4],
        #                  [2][0], [2][1], [2][2], [2][3], [2][4],
        #                  [3][0], [3][1], [3][2], [3][3], [3][4],  # 모서리쪽 칸
        #                  [4][0], [4][1],
        #                  [5][0], [5][1],
        #                  [6][0], [6][1],
        #                  [7][0], [7][1]]  # 가운데쪽 칸
        # self.turn = '1'  # 플레이어의 턴 저장 변수 '1' 이면 1player, '2'이면 2player
        # self.yutcount = 0 #누적 윷 갯수
        # self.canthow = 0 # 윷 던질 수 있는 횟수

        # 윷 확률 : 개(30%) 걸(26%) 도(12%) 빽도(12%) 낙(10%) 윷(5%) 모(5%)
        for i in range(100):
            if i < 30:
                self.yutrandoms.append(2)  # 개
            elif i < 56:
                self.yutrandoms.append(3)  # 걸
            elif i < 68:
                self.yutrandoms.append(1)  # 도
            elif i < 80:
                self.yutrandoms.append(-1)  # 빽도
            elif i < 90:
                self.yutrandoms.append(0)  # 낙
            elif i < 95:
                self.yutrandoms.append(4)  # 윷
            else:
                self.yutrandoms.append(5)  # 모

    # 이동할 칸 수를 리턴하는 메소드
    def throw(self):

        # 난수로 yuts의 자리값 선택
        resultnum = random.randint(0, 99)
        self.resultyut = ''

        if self.yutrandoms[resultnum] == -1:
            self.resultyut = "빽도"
        elif self.yutrandoms[resultnum] ==0:
            self.resultyut =  '낙'
        elif self.yutrandoms[resultnum] == 1:
            self.resultyut = '도'
        elif self.yutrandoms[resultnum] == 2:
            self.resultyut = '개'
        elif self.yutrandoms[resultnum] == 3:
            self.resultyut = '걸'
        elif self.yutrandoms[resultnum] == 4:
            self.resultyut = '윷'
        elif self.yutrandoms[resultnum] == 5:
            self.resultyut = '모'

        # 이동 칸 수 반환
        # return self.yutrandoms[resultnum]


    ## 아래 함수들은 아직 메인함수랑 연동했을 때 오류가 떠서 주석처리 해놨습니다! ##


    #말 움직이는 함수
    # def moveButton(self):
    #     if self.pYut == '빽도':
    #         for i,j in self.yutArray:
    #             self.savePlayer = [i][j] # 말의 현재위치
    #             self.savePlayer = self.savePlayer[i][j-1]
    #             #출발점일 땐 이동 안함
    #             if self.player1_1 == self.player1_1[0][0]:
    #                 self.savePlayer = self.savePlayer[0][0]
    #             #예외상황
    #             elif self.savePlayer == self.savePlayer[1][0]:
    #                 self.savePlayer = self.yutArray[0][4]
    #             elif self.savePlayer == self.savePlayer[4][0]:
    #                 self.savePlayer = self.yutArray[0][4]
    #             elif self.savePlayer == self.savePlayer[2][0]:
    #                 self.savePlayer = self.yutArray[1][4]
    #             elif self.savePlayer == self.savePlayer[5][0]:
    #                 self.savePlayer = self.yutArray[1][4]
    #             elif self.savePlayer == self.savePlayer[3][0]:
    #                 self.savePlayer = self.yutArray[2][4]
    #             elif self.savePlayer == self.savePlayer[7][1]:
    #                 self.savePlayer = self.yutArray[2][4]
    #             break
    #     if self.pYut == '낙':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j]
    #     if self.pYut == '도':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j+1]
    #     if self.pYut == '개':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j+2]
    #     if self.pYut == '걸':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j+3]
    #     if self.pYut == '윷':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j+4]
    #     if self.pYut == '모':
    #         for i,j in range in self.yutArray:
    #             self.savePlayer = self.savePlayer[i][j+5]

    #턴 옮기는 함수 구현 후 더 구현할 예정
    # def location(self):
    #     self.shortcut = bool('지름길') #지름길 판별
    #     #1P 첫번째 지름길
    #     if self.player1_1 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_2 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_3 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_4 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     #1P 두번째 지름길
    #     elif self.player1_1 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_2 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_3 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player1_4 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     #2P 첫번째 지름길
    #     elif self.player2_1 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_2 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_3 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_4 == self.yutArray[0][4]:
    #         self.shortcut = '지름길'
    #     #2P 두번째 지름길
    #     elif self.player2_1 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_2 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_3 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #     elif self.player2_4 == self.yutArray[1][4]:
    #         self.shortcut = '지름길'
    #
    #     return self.shortcut
    #
    # #골판정 함수
    # def Goal(self):
    #     self.goal_1p = 0
    #     self.goal_2p = 0
    #     if self.player1_1 == self.yutArray[3][4]:
    #         self.goal_1p = self.goal_1p + 1
    #     elif self.player1_2 == self.yutArray[3][4]:
    #         self.goal_1p = self.goal_1p + 1
    #     elif self.player1_3 == self.yutArray[3][4]:
    #         self.goal_1p = self.goal_1p + 1
    #     elif self.player1_4 == self.yutArray[3][4]:
    #         self.goal_1p = self.goal_1p + 1
    #
    #     if self.player2_1 == self.yutArray[3][4]:
    #         self.goal_2p = self.goal_2p + 1
    #     elif self.player2_2 == self.yutArray[3][4]:
    #         self.goal_2p = self.goal_2p + 1
    #     elif self.player2_3 == self.yutArray[3][4]:
    #         self.goal_2p = self.goal_2p + 1
    #     elif self.player2_4 == self.yutArray[3][4]:
    #         self.goal_2p = self.goal_2p + 1
    #
    #     return self.goal_1p, self.goal_2p
    #
    # #게임 종료
    # def GameOver(self):
    #     self.text #승리 메세지 변수
    #     if self.goal_1p == 4:
    #         self.text = "플레이어 1이 이겼습니다!"
    #     elif self.goal_2p == 4:
    #         self.text = "플레이어 2가 이겼습니다!"


# player1 = Yut()
# print(player1.throw())
# print(player1.pYut)