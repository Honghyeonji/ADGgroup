# 업기 함수를 만들 연습파일

# 업기함수를 3개로 나누었습니다. 1개->2개, 2개->3개, 3개->4개
# 그래서 업기 전에 현재 말이 1개인지 2개인지(1개를 업음) 3개인지(2개를 업음) 상태에 따라 알맞는 업기함수를 선택해서 하도록 해야할 것 같습니다.
# 현재 말의 이미지를 검사하여 하는 등의 방법이 있을 것 같습니다.
# 현지님이 올려주셨던 move함수와 관계를 생각하며 업기 코드를 짜보았습니다. 그런데 부족한 부분이 많기 때문에 안되는 부분 or 이해 안되는 부분 바로 알려주시면 감사하겠습니다.



class Player:
    def __init__(self):

        # 이동 함수에서만 쓰일 pYut = 0  # 사용자의 도,개,걸,윷,모,빽도,낙의 이동해야할 칸수를 저장합니다.
        # -> 이동함수 인자로 이동시킬 플레이어말넘버와 윷 결과를 넣고
        # -> 아래의 self.yuts 딕으로 이동시킬 칸을 찾아 pYut에 넣고 그 값에 따라 이동하게
        self.yutrandoms = []  # 확률 구성 리스트
        self.yuts = {"빽도":-1, "낙":0, "도":1, "개":2, "걸":3, "윷":4, "모":5}
        self.name = '' # 플레이어 닉네임
        self.resultyut = ''
        self.mapcan = {'00': "empty", '01': "empty", '02': "empty", '03': "empty", '04': "empty",
                        '10': "empty", '11': "empty", '12': "empty", '13': "empty", '14': "empty",
                        '20': "empty", '21': "empty", '22': "empty", '23': "empty", '24': "empty",
                        '30': "empty", '31': "empty", '32': "empty", '33': "empty", '34': "empty",
                        '40': "empty", '41': "empty",
                        '50': "empty", '51': "empty",
                        '60': "empty", '61': "empty",
                        '70': "empty", '71': "empty", }  # - 맵 현재상태(비었는지말이있는지)

        self.playerLocation = {'player1': "noLocation", "player2": "noLocation", "player3": "noLocation",
                               "player4": "noLocation",
                               "player12": "noLocation", "player13": "noLocation", "player14": "noLocation",
                               "player23": "noLocation", "player24": "noLocation", "player34": "noLocation",
                               "player123": "noLocation", "player134": "noLocation", "player234": "noLocation",
                               "player1234": "noLocation", }  # - 플레이어가 현재있는칸의위치

        #self.playerimage = {"player1": 'image:url(player1_1.png)', }  #

        def upgi(self, mal,inputplayer):  # 말 1개를 업음 (말 2개)
            # 여기서 mal은 현재 움직인 말 nowplayer
            pL = list(self.playerLocation.values())  # 말들의 현재 위치를  리스트로 생성

            for i in range(len(pL)):
                if mal == pL[i]:  # 현재 말과 위치가 같은 말 발견
                    if i == 0:  # 같은 위치의 말이 player1 말 ->self.playerLocation[0]은 'player1'의 value값이기 때문입니다.
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[4] = self.playerLocation[mal] # 말 업은 이미지 경우의 수가 더 많은데 현재 말이 몇번 째 말인지(무슨 색인지)구분할 수 없어서 그냥 'player12'로 하였습니다.
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 12
                        return inputplayer
                    elif i == 1:
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[7] = self.playerLocation[mal]
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 23
                        return inputplayer
                    elif i == 2:
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[5] = self.playerLocation[mal]
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 13
                        return inputplayer
                    elif i == 3:
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[6] = self.playerLocation[mal]
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 14
                        return inputplayer
                    else:
                        continue

        def upgi2(self, mal,inputplayer):  # 말 2개를 업음 (말 3개)
            pL = list(self.playerLocation.values())
            for i in range(len(pL)):
                if mal == pL[i]:
                    if i == 4:  # 12
                        self.playerLocation[10] = self.playerLocation[mal]
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 123
                        return inputplayer

                    elif i == 5:  # 13
                        self.playerLocation[11] = self.playerLocation[mal]
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 134
                        return inputplayer
                    elif i == 6:  # 14
                        self.playerLocation[11] = self.playerLocation[mal]
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 134
                        return inputplayer
                    elif i == 7:  # 23
                        self.playerLocation[12] = self.playerLocation[mal]
                        self.playerLocation[i] = "noLocation"
                        self.playerLocation[mal] = "noLocation"
                        inputplayer = 234
                        return inputplayer
                    else:
                        continue
                    # elif i == 8:
                    # elif i == 9:

        def upgi3(self, mal,inputplayer):  # 말 3개를 업음 (말 4개)
            self.playerLocation[13] = self.playerLocation[mal]
            self.playerLocation[mal] = "noLocation"
            inputplayer = 1234
            return inputplayer


        # 현지님이 올려주신 이동함수 입니다.
        def move(self, inputplayer):
            #inputplayer는 플레이어 말
            oldplayer = self.playerLocation[inputplayer]
            nowplayer = self.playerLocation[inputplayer]
            if(nowplayer[1]<"4"): #외곽선 이동시
                nowplayer = str(int(nowplayer) + self.pyut)
                if(nowplayer[1] > "4"): #꺾여진 선 이동
                    if(nowplayer[0] == "3"):
                        pass
                    #마지막 줄이었을 경우 골인
                    else:
                        nowplayer = str(int(nowplayer) - 4 + 10)
            elif(nowplayer[1] == "4"): #대각선 진입시
                if nowplayer[0] == "3":
                    pass
                #대각선 진입 x
                else:
                    pass# 대각선 진입
            elif nowplayer[0] in range(4,8):
                pass
            #대각선에 있을 경우
            elif(nowplayer[0] == maincan):
                pass
            #정가운데 칸에 있을 경우

            pL = list(self.playerLocation.values()) # 말들의 현재 위치를 가진 리스트를 생성
            if(nowplayer in pL): # 리스트에 현재 움직인 말의 위치와 같은 말이 있다면 업기 실행 (현재 pL에 현재 움직인 말의 위치정보가 업데이트 되지 않았음)
                self.upgi(nowplayer,inputplayer)
                # 위치정보가 같은 말이 하나도 없으면 그냥 이동한다.

            #이 안에서 함수 연계해서 말잡기, 말업기 기능 추가

            self.mapcan[oldplayer] = "empty"
            self.mapcan[nowplayer] = inputplayer #맵 정보 갱신
            self.playerLocation[inputplayer] = nowplayer # 플레이어 말 각각의 위치 정보 갱신

            return oldplayer, nowplayer, self.playerimg[inputplayer]