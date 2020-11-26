import random
# 난수 발생을 위해 random 라이브러리 사용

class Yut:
    def __init__(self):

        self.pYut = ''  # 사용자의 도,개,걸,윷,모,빽도,낙의 결과를 저장합니다.
        self.yuts = []  # 확률 구성 리스트
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
        self.yutArray = [[0][0], [0][1], [0][2], [0][3], [0][4],
                         [1][0], [1][1], [1][2], [1][3], [1][4],
                         [2][0], [2][1], [2][2], [2][3], [2][4],
                         [3][0], [3][1], [3][2], [3][3], [3][4],  # 모서리쪽 칸
                         [4][0], [4][1],
                         [5][0], [5][1],
                         [6][0], [6][1],
                         [7][0], [7][1]]  # 가운데쪽 칸
        self.turn = '1'  # 플레이어의 턴 저장 변수 '1' 이면 1player, '2'이면 2player
        self.yutcount = 0 #누적 윷 갯수
        self.canthow = 0 # 윷 던질 수 있는 횟수

        # 윷 확률 : 개(30%) 걸(26%) 도(12%) 빽도(12%) 낙(10%) 윷(5%) 모(5%)
        for i in range(100):
            if i < 30:
                self.yuts.append(2)  # 개
            elif i < 56:
                self.yuts.append(3)  # 걸
            elif i < 68:
                self.yuts.append(1)  # 도
            elif i < 80:
                self.yuts.append(-1)  # 빽도
            elif i < 90:
                self.yuts.append(0)  # 낙
            elif i < 95:
                self.yuts.append(4)  # 윷
            else:
                self.yuts.append(5)  # 모

    # 이동할 칸 수를 리턴하는 메소드
    def throw(self):

        # 난수로 yuts의 자리값 선택
        result = random.randint(0, 99)

        if self.yuts[result] == -1:
            self.pYut = '빽도'
        elif self.yuts[result] == 0:
            self.pYut = '낙'
        elif self.yuts[result] == 1:
            self.pYut = '도'
        elif self.yuts[result] == 2:
            self.pYut = '개'
        elif self.yuts[result] == 3:
            self.pYut = '걸'
        elif self.yuts[result] == 4:
            self.pYut = '윷'
        elif self.yuts[result] == 5:
            self.pYut = '모'

        # 이동 칸 수 반환
        return self.yuts[result]


    #턴 옮기는 함수 구현 후 더 구현할 예정
    def location(self):
        self.shortcut = bool('지름길') #지름길 판별
        #1P 첫번째 지름길
        if self.player1_1 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player1_2 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player1_3 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player1_4 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        #1P 두번째 지름길
        elif self.player1_1 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player1_2 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player1_3 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player1_4 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        #2P 첫번째 지름길
        elif self.player2_1 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player2_2 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player2_3 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        elif self.player2_4 == self.yutArray[0][4]:
            self.shortcut = '지름길'
        #2P 두번째 지름길
        elif self.player2_1 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player2_2 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player2_3 == self.yutArray[1][4]:
            self.shortcut = '지름길'
        elif self.player2_4 == self.yutArray[1][4]:
            self.shortcut = '지름길'

        return self.shortcut

    #골판정 함수
    def Goal(self):
        self.goal_1p = 0
        self.goal_2p = 0
        if self.player1_1 == self.yutArray[3][4]:
            self.goal_1p = self.goal_1p + 1
        elif self.player1_2 == self.yutArray[3][4]:
            self.goal_1p = self.goal_1p + 1
        elif self.player1_3 == self.yutArray[3][4]:
            self.goal_1p = self.goal_1p + 1
        elif self.player1_4 == self.yutArray[3][4]:
            self.goal_1p = self.goal_1p + 1

        if self.player2_1 == self.yutArray[3][4]:
            self.goal_2p = self.goal_2p + 1
        elif self.player2_2 == self.yutArray[3][4]:
            self.goal_2p = self.goal_2p + 1
        elif self.player2_3 == self.yutArray[3][4]:
            self.goal_2p = self.goal_2p + 1
        elif self.player2_4 == self.yutArray[3][4]:
            self.goal_2p = self.goal_2p + 1

        return self.goal_1p, self.goal_2p

    #게임 종료
    def GameOver(self):
        self.text #승리 메세지 변수
        if self.goal_1p == 4:
            self.text = "플레이어 1이 이겼습니다!"
        elif self.goal_2p == 4:
            self.text = "플레이어 2가 이겼습니다!"


player1 = Yut()
print(player1.throw())
print(player1.pYut)
