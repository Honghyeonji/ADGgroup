    #말 움직이는 함수
    def moveButton(self, inputplayer):
        self.mapcan = {'00': "empty", '01': "empty", '02': "empty", '03': "empty", '04': "empty",
                        '10': "empty", '11': "empty", '12': "empty", '13': "empty", '14': "empty",
                        '20': "empty", '21': "empty", '22': "empty", '23': "empty", '24': "empty",
                        '30': "empty", '31': "empty", '32': "empty", '33': "empty", '34': "empty",
                        '40': "empty", '41': "empty",
                        '50': "empty", '51': "empty",
                        '60': "empty", '61': "empty",
                        '70': "empty", '71': "empty", }

        self.playerLocation = {'player1_1': "noLocation", "player1_2": "noLocation", "player1_3": "noLocation",
                               "player1_4": "noLocation",
                               "player1_12": "noLocation", "player1_13": "noLocation", "player1_14": "noLocation",
                               "player1_23": "noLocation", "player1_24": "noLocation", "player1_34": "noLocation",
                               "player1_123": "noLocation", "player1_134": "noLocation", "player1_234": "noLocation",
                               "player1_1234": "noLocation", }
        pL = list(self.playerLocation.values())
        
        oldplayer = self.playerLocation[inputplayer]
        nowplayer = self.playerLocation[inputplayer]
        goal = True
        goalplayer = 0
        if(nowplayer[1] < "04"): #외각선 이동시
            nowplayer = str(int(nowplayer) + self.yuts)
            if(nowplayer[1] > "04"): #꺾여진 선 이동
                nowplayer = str(int(nowplayer) - 4 + 10 + self.yuts)
                if(nowplayer[0] == "03"): #마지막 줄이었을 경우 골인
                    nowplayer = bool(goal)
                    self.playerLocation[nowplayer] = "noLocation"
                    goalplayer + 1
                elif goalplayer == 4: #골한 플레이어가 4명인 경우 게임 종료
                    self.close()
                else: nowplayer = str(int(nowplayer) - 4 + 10)
        elif(nowplayer[1] == "04"): #대각선 진입시
            nowplayer = str(int(nowplayer) - 4 + 40 + self.yuts)
            if(nowplayer[0] == "03"): #대각선 진입 X
                nowplayer = str(int(nowplayer) - 3 + 10 + self.yuts)
            else: #첫번째 대각선 진입
                nowplayer  = str(int(nowplayer) - 4 + 40 + self.yuts)
        elif(nowplayer[1] == "14"): #두번째 대각선 진입
            nowplayer = str(int(nowplayer) - 14 + 50 + self.yuts)
            if(nowplayer[0] == "13"): #대각선 진입 X
                nowplayer = str(int(nowplayer) - 13 + 20 + self.yuts)
            else: #첫번째 대각선 진입
                nowplayer  = str(int(nowplayer) - 14 + 50 + self.yuts)
        elif (nowplayer[0] in range(4, 8)):  # 첫번째 대각선에 있을 경우
            if (self.yuts <= '2'):  # 플레이어가 메인칸 전일 때
                nowplayer = str(int(nowplayer) + self.yuts)
            
            elif (self.pYut == '웇'): #대각선 칸에서 윷이 나온 경우
                nowplayer = str(int(nowplayer) - nowplayer + 70)
            elif (self.pYut == '모'): #대각선 칸에서 모가 나온 경우
                nowplayer = str(int(nowplayer) - nowplayer + 71)
                
        elif (nowplayer[0] in range(4, 8)):  # 두번째 대각선에 있을 경우
            if (self.yuts <= '2'):  # 플레이어가 메인칸 전일 때
                nowplayer = str(int(nowplayer) + self.yuts)
            
            elif (self.pYut == '웇'): #대각선 칸에서 윷이 나온 경우
                nowplayer = str(int(nowplayer) - nowplayer + 60)
            elif (self.pYut == '모'): #대각선 칸에서 모가 나온 경우
                nowplayer = str(int(nowplayer) - nowplayer + 61)
                
        elif(nowplayer[0] == self.maincan): # 정가운데 칸이 있을 경우
            if(oldplayer == '40' or oldplayer == '41'): #이전 말이 40이나 41위치에 있을 경우 대각선 진입
                nowplayer = str(int(nowplayer) - nowplayer + self.yuts)
            else: #이전 말이 50이나 51 위치에 있을 경우
                nowplayer = str(int(nowplayer) - nowplayer + self.yuts)

        self.mapcan[oldplayer] = "empty"
        self.mapcan[nowplayer] = inputplayer #맵 정보 갱신
        self.playerLocation[inputplayer] = nowplayer #플레이어 각각의 정보 갱신

        return oldplayer, nowplayer, self.playerLocation[inputplayer]
