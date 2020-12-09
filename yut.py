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

        self.pYut = 0  # 도개걸윷모낙빽도 결과 이동해야할 칸 수로 저장
        self.yutRandoms = []  # 확률 구성 리스트
        self.name = ''  # 플레이어 닉네임
        self.resultYut = ''  # 도개걸윷모낙빽도 결과 문자열로 저장
        self.goalplayer = 0  # 골인한 말의 수 - main.py에서 move이벤트 한 후에 goal판정하는 데에 쓰일 변수

        # self.canthow = 0 # 윷 던질 수 있는 횟수

        self.mapCan = {'11': "empty", '12': "empty", '13': "empty", '14': "empty", '15': "empty",
                       '21': "empty", '22': "empty", '23': "empty", '24': "empty", '25': "empty",
                       '31': "empty", '32': "empty", '33': "empty", '34': "empty", '35': "empty",
                       '41': "empty", '42': "empty", '43': "empty", '44': "empty", '45': "empty",
                       '51': "empty", '52': "empty",
                       '61': "empty", '62': "empty",
                       '71': "empty", '72': "empty",
                       '81': "empty", '82': "empty",
                       '90': "empty"}  # 90은 제일 가운데 칸

        self.playerLocation = {'player1': "noLocation", "player2": "noLocation", "player3": "noLocation",
                               "player4": "noLocation",
                               "player12": "noLocation", "player13": "noLocation", "player14": "noLocation",
                               "player23": "noLocation", "player24": "noLocation", "player34": "noLocation",
                               "player123": "noLocation", "player134": "noLocation", "player234": "noLocation",
                               "player1234": "noLocation", }

        # 윷 확률 : 개(30%) 걸(26%) 도(12%) 빽도(12%) 낙(10%) 윷(5%) 모(5%)
        for i in range(100):
            if i < 30:
                self.yutRandoms.append(2)  # 개
            elif i < 56:
                self.yutRandoms.append(3)  # 걸
            elif i < 68:
                self.yutRandoms.append(1)  # 도
            elif i < 80:
                self.yutRandoms.append(-1)  # 빽도
            elif i < 90:
                self.yutRandoms.append(0)  # 낙
            elif i < 95:
                self.yutRandoms.append(4)  # 윷
            else:
                self.yutRandoms.append(5)  # 모

    # 이동할 칸 수를 리턴하는 메소드
    def throw(self):
        resultNum = random.randint(0, 99)  # 난수로 yuts의 자리값 선택
        self.resultYut = ''

        if self.yutRandoms[resultNum] == -1:
            self.resultYut = "빽도"
            self.pYut = -1
        elif self.yutRandoms[resultNum] == 0:
            self.resultYut = '낙'
            self.pYut = 0
        elif self.yutRandoms[resultNum] == 1:
            self.resultYut = '도'
            self.pYut = 1
        elif self.yutRandoms[resultNum] == 2:
            self.resultYut = '개'
            self.pYut = 2
        elif self.yutRandoms[resultNum] == 3:
            self.resultYut = '걸'
            self.pYut = 3
        elif self.yutRandoms[resultNum] == 4:
            self.resultYut = '윷'
            self.pYut = 4
        elif self.yutRandoms[resultNum] == 5:
            self.resultYut = '모'
            self.pYut = 5


    # 말 움직이는 함수
    def move(self, inputplayer, rivalLocation):  # 라이벌로케이션은 이대로 말 잡기에서 수정되어서 리턴될 것임

        # 빽도였을 경우와 낙일경우도 추가해야함

        oldplayer = self.playerLocation[inputplayer]  # 원래 말이 서있던 위치
        nowplayer = self.playerLocation[inputplayer]  # 현재 말이 어느 위치에 서있는지

        # 외곽선 이동, 1, 2번 줄인데 모서리에 안서있는 경우(모서리에 서있으면 대각전 진입) 혹은 3, 4번 줄일 경우
        # nowplayer는 현재 말의 위치라서 "OO" 형식, 첫번째 숫자는 몇번째 선에 있는지, 두번째 숫자는 그 선의 몇 번째 칸에 있는지를 표현
        if ((1 <= int(nowplayer[0]) <= 2) and (int(nowplayer[1]) < 5)) or (3 <= int(nowplayer[0]) <= 4):
            # 마지막 줄이었을 경우
            if nowplayer[0] == "4":
                nowplayer = str(int(nowplayer) + self.pYut)
                # 말이 서있어야할 위치가 마지막 줄의 마지막 칸을 넘겼다면 골인
                if int(nowplayer[1]) > 5:
                    self.playerLocation[inputplayer] = "noLocation"  # 현재 말의 위치 정보에서 위치 없앰
                    self.goal(inputplayer)  # 몇개의 말이 골을 했는지 판정 -> 골한 말의 수 갱신
                    self.mapCan[oldplayer] = "empty"  # 현재 칸의 상태에서 원래 말이 서있던 위치 비움

            # 마지막 줄이 아니였을 경우
            else:
                nowplayer = str(int(nowplayer) + self.pYut)
                # 꺾여진 선 이동 (n번째 줄에서 n+1번째 줄로 넘어갈 때)
                if int(nowplayer[1]) > 5:
                    nowplayer = str(int(nowplayer) - 5 + 10 + self.pYut)

        # 1번째 줄 모서리에서 대각선 진입
        elif nowplayer == "15":
            nowplayer = str(int(nowplayer) - 5 + 40 + self.pYut)  # 일단 5번째 줄로 이동
            if nowplayer[1] == "3":  # 대각선들 줄은 칸의 수가 2개씩 밖에 없기 때문에 두번째 숫자가 3일 경우 가운데 칸
                nowplayer = "90"
            elif 4 <= int(nowplayer[1]) <= 5:  # 두번째 숫자가 4 or 5일 경우 7번째 줄로 재설정(이어지는 대각선)
                nowplayer = str(int(nowplayer) - 3 + 20)
        # 2번째 줄 모서리에서 대각선 진입
        elif nowplayer == "25":
            # 위 코드와 동일
            nowplayer = str(int(nowplayer) - 5 + 40 + self.pYut)
            if nowplayer[1] == "3":
                nowplayer = "90"
            elif 4 <= int(nowplayer[1]) <= 5:
                nowplayer = str(int(nowplayer) - 3 + 20)

        # 대각선에 있을 경우
        elif int(nowplayer[0]) in range(5, 10):
            # 플레이어말이 메인칸 전 대각선에 있을 경우 (5번째, 6번째 줄에 있을 경우)
            if int(nowplayer[0]) in range(5, 7):
                nowplayer = str(int(nowplayer) + self.pYut)
                if nowplayer[1] == "3":
                    nowplayer = "90"
                elif 4 <= int(nowplayer[1]) <= 5:
                    nowplayer = str(int(nowplayer) - 3 + 20)
                # 두번째 숫자가 6일 경우
                elif nowplayer[1] == "6":
                    if nowplayer[0] == "5":  # 5번째줄(오른쪽 위 대각선)에 있던 플레이어말은 왼쪽 아래 꼭짓점칸으로 이동
                        nowplayer = "35"
                    elif nowplayer[0] == "6":  # 6번째줄(왼쪽 위 대각선)에 있던 플레이어말은 골인위치로 이동
                        nowplayer = "45"
                # 두번째 숫자가 7이상일 경우
                elif int(nowplayer[1]) >= 7:
                    if nowplayer[0] == "5":  # 5번째줄(오른쪽 위 대각선)에 있던 플레이어말은 외곽 마지막줄로 이동
                       nowplayer = str(int(nowplayer) - 16)
                    elif nowplayer[0] == "6":  # 6번째줄(왼쪽 위 대각선)에 있던 플레이어말은 골인
                        self.playerLocation[inputplayer] = "noLocation"
                        self.goal(inputplayer)
                        self.mapCan[nowplayer] = "empty"

            # 플레이어말이 메인칸 후 대각선에 있을 경우 (7번째, 8번째 줄에 있을 경우)
            elif int(nowplayer[0]) in range(7, 9):
                nowplayer = str(int(nowplayer) + self.pYut)
                if nowplayer[1] == "3":  # 두번째 숫자가 3일 경우
                    if nowplayer[0] == "7":  # 7번째줄(왼쪽 아래 대각선)에 있던 플레이어 말은 왼쪽 아래 꼭짓점칸으로 이동
                        nowplayer = "35"
                    elif nowplayer[0] == "8":  # 8번째줄(오른쪽 아래 대각선)에 있던 플레이어 말은 오른쪽 아래 꼭짓점칸으로 이동
                        nowplayer = "45"
                elif int(nowplayer[1]) > 3:  # 두번째 숫자가 3 이상일 경우 - 외곽선 가운데에 위치해있어야함
                    if nowplayer[0] == "7":  # 7번째줄(왼쪽 아래 대각선)에 있던 플레이어 말은 외곽 마지막줄로 이동동
                        nowplayer = str(int(nowplayer) - 33)
                    if nowplayer[0] == "8":  # 8번째줄(오른쪽 아래 대각선)에 있던 플레이어 말은 골인
                        self.playerLocation[inputplayer] = "noLocation"
                        self.goal(inputplayer)
                        self.mapCan[nowplayer] = "empty"

            elif nowplayer == "90":  # 정가운데 칸에 있을 경우
                nowplayer = str(80 + self.pYut)  # 무조건 골쪽으로 이동해야하니 8번째 줄에서부터 시작(80에서 시작)
                if nowplayer == "83":  # 83일경우 골인지점에 위치
                    nowplayer = "45"
                elif int(nowplayer[1]) > 3:  # 골인
                    self.playerLocation[inputplayer] = "noLocation"
                    self.goal(inputplayer)
                    self.mapCan[nowplayer] = "empty"

        # 말업기가 됐을 경우 현재플레이어말 갱신,
        inputplayer = self.upgi(inputplayer, nowplayer)

        self.mapCan[oldplayer] = "empty"
        self.mapCan[nowplayer] = inputplayer  # 맵 정보 갱신
        self.playerLocation[inputplayer] = nowplayer  # 플레이어 각각의 정보 갱신

        return oldplayer, nowplayer, self.playerLocation[inputplayer]

    def upgi(self, mal, nowLocation):

        # 여기서 mal은 현재 이동중인 플레이어말, nowLocation은 플레이어말의 이동 될 위치
        # pL = list(self.playerLocation.values())  # 말들의 현재 위치를  리스트로 생성

        if len(mal[6:]) == 1:  # 입력된 말이 하나일 경우
            for key, value in self.playerLocation.items():
                if nowLocation == value:  # 현재 말과 위치가 같은 말 발견
                    if key == mal:  # 현재 말과 위치가 같은 말이 현재 말과 같은 말일 경우 그냥 리턴 아무것도 안하고 리턴
                        return
                    elif key != mal:
                        if (key == "player1" and mal == "player2") or (key == "player2" and mal == "player1"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = "player12"
                            return mal
                        elif (key == "player2" and mal == "player3") or (key == "player3" and mal == "player2"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player23'
                            return mal
                        elif (key == "player1" and mal == "player3") or (key == "player3" and mal == "player1"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player13'
                            return mal
                        elif (key == "player1" and mal == "player4") or (key == "player4" and mal == "player1"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player14'
                            return mal
                        elif (key == "player2" and mal == "player4") or (key == "player4" and mal == "player2"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player24'
                            return mal
                        elif (key == "player3" and mal == "player4") or (key == "player4" and mal == "player3"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player34'
                            return mal
                        elif (key == "player23" and mal == "player1") or (key == "player13" and mal == "player2") or (
                                key == "player12" and mal == "player3"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player123'
                            return mal
                        elif (key == "player24" and mal == "player1") or (key == "player14" and mal == "player2") or (
                                key == "player12" and mal == "player4"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player124'
                            return mal
                        elif (key == "player34" and mal == "player1") or (key == "player13" and mal == "player4") or (
                                key == "player14" and mal == "player3"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player134'
                            return mal
                        elif (key == "player23" and mal == "player4") or (key == "player34" and mal == "player2") or (
                                key == "player24" and mal == "player3"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player234'
                            return mal
                        elif (key == "player234" and mal == "player1") or (key == "player134" and mal == "player2") or (
                                key == "player124" and mal == "player3") or (key == "player123" and mal == "player4"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player1234'
                            return mal

        elif len(mal[6:]) == 2:  # 입력된 말이 두개일 경우
            for key, value in self.playerLocation.items():
                if nowLocation == value:
                    if key == mal:
                        return
                    elif key != mal:
                        if (key == "player1" and mal == "player23") or (key == "player2" and mal == "player13") or (
                                key == "player3" and mal == "player12"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player123'
                            return mal
                        elif (key == "player1" and mal == "player24") or (key == "player2" and mal == "player14") or (
                                key == "player4" and mal == "player12"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player124'
                            return mal
                        elif (key == "player1" and mal == "player34") or (key == "player3" and mal == "player14") or (
                                key == "player4" and mal == "player13"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player134'
                            return mal
                        elif (key == "player2" and mal == "player34") or (key == "player3" and mal == "player24") or (
                                key == "player4" and mal == "player23"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player234'
                            return mal
                        elif (key == "player12" and mal == "player34") or (key == "player13" and mal == "player24") or (
                                key == "player14" and mal == "player23") or (
                                key == "player23" and mal == "player14") or (
                                key == "player24" and mal == "player13") or (key == "player34" and mal == "player12"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player1234'
                            return mal

        elif len(mal[6:]) == 3:
            for key, value in self.playerLocation.items():
                if nowLocation == value:
                    if key == mal:
                        return
                    elif key != mal:
                        if (key == "player1" and mal == "player234") or (key == "player2" and mal == "player134") or (
                                key == "player3" and mal == "player124") or (key == "player4" and mal == "player123"):
                            self.playerLocation[key] = "noLocation"
                            self.playerLocation[mal] = "noLocation"
                            mal = 'player1234'
                            return mal

    # 플레이어말의 수에 따라(업고있는 말일 수 있으니) 골한 플레이어 추가
    def goal(self, inputplayer):
        if len(inputplayer[6:]) == 1:
            self.goalplayer += 1
        elif len(inputplayer[6:]) == 2:
            self.goalplayer += 2
        elif len(inputplayer[6:]) == 3:
            self.goalplayer += 3
        elif len(inputplayer[6:]) == 4:
            self.goalplayer += 4
