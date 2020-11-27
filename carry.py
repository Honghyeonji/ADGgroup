# 업기 함수를 만들 파일
'''
1.윷을 던진다
2.사용자는 움직일 말을 고른다
3.말의 좌표가 윷 결과에 따라 이동한다.
4.만약 이동할 칸에 함수 upgi를 실행한다. upgi(nowMal, mapMal)
5.현재의 말은 0,0 좌표로 돌아가지만 인터페이스 상에서는 기존에 있었던 팀의 말 위에 업힌 것처럼 출력한다.
6.기존 판에 있었던 말은 이미지가 업혀진 말로 변경이 된다. upgi_img(mapMal)
7. 그 상태로 출발점으로 돌아오면 if문으로 검사하여 이미지에 따라 스코어를 받는다.

판에 이미 있던 말 - A, 새로 판에 둘 말 - B

if A[?][?] == B[?][?]
    B = [0][0]
    A => 말2개로 이미지 변경

goal 지점에서 이미지 검사로 스코어 증가?
각 칸 배열 마다 고유값 설정 필요함
이미 2~3개를 업은 상태에서 2~1개를 더 업는다면?
'''

def upgi(self, nowP, mapP):  # nowP : 현재 움직일 말, mapP : 현재 맵 좌표에 있는 말
    if nowP == self.player1_1:
        if mapP == self.player1_2:
            # 이미지에 따라 도착지점에서 올라갈 스코어 확인?
            self.player1_1 = self.yutArray[0][0] # 1번째 말은 2번째 말에 업은 것 처럼 보이지만 맵 처음으로 돌려보냄.
            upgi_img(mapP)                        # 이후에 잡혀서 원점으로 돌아오지 않는 이상 사용할 수 X 인터페이스에 표시되지 않음.


        elif mapP == self.player1_3:
            self.player1_1 = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_4:
            self.player1_1 = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player1_2:
        if mapP == self.player1_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_3:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_4:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player1_3:
        if mapP == self.player1_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_2:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_4:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player1_4:
        if mapP == self.player1_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_2:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player1_3:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player2_1:
        if mapP == self.player2_2:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_3:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_4:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player2_2:
        if mapP == self.player2_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_3:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_4:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player2_3:
        if mapP == self.player2_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_2:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_4:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

    elif nowP == self.player2_4:
        if mapP == self.player2_1:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_2:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)

        elif mapP == self.player2_3:
            self.nowP = self.yutArray[0][0]
            upgi_img(mapP)


#def upgi_img(self,nowP, mapP):
    # 말 2개가 업혀진 이미지 변경 ex)image:url('upgi2.png')

        # if image == 'image:url(player1_1.png)': #만약 플레이어가 아무것도 업지 않은 상태라면
            # image = 'image:url(upgi2.png) # 1개 업은 이미지로 변경
            # elif image == 'image:url(upgi2.png)': # 만약 플레이어가 이미 1개를 업은 상태라면
            # image = 'image:url(upgi3.png)' # 2개 업은 이미지로 변경
