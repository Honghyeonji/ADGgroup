    def upgi(self, mal, inputplayer):  # 말 1개를 업음 (말 2개)
        # 여기서 mal은 현재 움직인 말 nowplayer
        pL = list(self.playerLocation.values())  # 말들의 현재 위치를  리스트로 생성
        self.chance = 0

        for i in range(len(pL)):
            if mal == pL[i]:  # 현재 말과 위치가 같은 말 발견
                if i == 0:  # 같은 위치의 말이 player1 말 ->self.playerLocation[0]은 'player1'의 value값이기 때문입니다.
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[4] = self.playerLocation[mal]  # 말 업은 이미지 경우의 수가 더 많은데 현재 말이 몇번 째 말인지(무슨 색인지)구분할 수 없어서 그냥 'player12'로 하였습니다.
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_12'
                    if nowplayer == self.playerLocation[4]: # (말 잡기 메소드) 현재 플레이어 위치가 업은 말의 위치랑 같을 때 업은 말의 위치는 사라짐
                        self.playerLocation[4] = "noLocation" 
                        self.chance = self.chance + 1 #던질 기회 추가 
                    return inputplayer, self.chance
                elif i == 1:
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[7] = self.playerLocation[mal]
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_23'
                    if nowplayer == self.playerLocation[7]:
                        self.playerLocation[7] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance
                elif i == 2:
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[5] = self.playerLocation[mal]
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_13'
                    if nowplayer == self.playerLocation[5]:
                        self.playerLocation[5] = "noLocation"
                        self.chance = self.chance = 1
                    return inputplayer, self.chance
                elif i == 3:
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[6] = self.playerLocation[mal]
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_14'
                    if nowplayer == self.playerLocation[6]:
                        self.playerLocation[6] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance
                else:
                    continue

    def upgi2(self, mal, inputplayer):  # 말 2개를 업음 (말 3개)
        pL = list(self.playerLocation.values())
        for i in range(len(pL)):
            if mal == pL[i]:
                if i == 4:  # 12
                    self.playerLocation[10] = self.playerLocation[mal]
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_123'
                    if nowplayer == self.playerLocation[10]:
                        self.playerLocation[10] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance

                elif i == 5:  # 13
                    self.playerLocation[11] = self.playerLocation[mal]
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_134'
                    if nowplayer == self.playerLocation[11]:
                        self.playerLocation[11] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance
                elif i == 6:  # 14
                    self.playerLocation[11] = self.playerLocation[mal]
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_134'
                    if nowplayer == self.playerLocation[11]:
                        self.playerLocation[11] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance
                elif i == 7:  # 23
                    self.playerLocation[12] = self.playerLocation[mal]
                    self.playerLocation[i] = "noLocation"
                    self.playerLocation[mal] = "noLocation"
                    inputplayer = 'player1_234'
                    if nowplayer == self.playerLocation[12]:
                        self.playerLocation[12] = "noLocation"
                        self.chance = self.chance + 1
                    return inputplayer, self.chance
                else:
                    continue
                # elif i == 8:
                # elif i == 9:

    def upgi3(self, mal, inputplayer):  # 말 3개를 업음 (말 4개)
        self.playerLocation[13] = self.playerLocation[mal]
        self.playerLocation[mal] = "noLocation"
        inputplayer = 'player1_1234'
        if nowplayer == self.playerLocation[13]:
            self.playerLocation = "noLocation"
            self.chance = self.chance + 1
        return inputplayer, self.chance
