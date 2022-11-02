class Player:
    property = "Player" # 클래스 변수

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.name) # 클래스 변수 출력

print(player.name) # name이라는 객체 변수가 없으면, 같은 이름의 클래스 변수가 선택돰.

Player.where(player) # 이게 원칙적인 파이썬의 멤버함수호출

player.where() # === Player.where(player)와 동일하다