# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{self.name} 유닛이 생성되었습니다.')
    
    def move(self, location):
        print(f'{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다.')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')

# 마린
class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정시간 동안 이동 및 공격 속도를 증가, 체력 10감소

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('f{self.name} : 스팀팩을 사용합니다. (HP 10 감소')
        else:
            print(f'{self.name} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.') 

# 탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈코드가 아닐 때 - > 시즈모드
        if self.set_seize_mode == False:
            print(f'{self.name} : 시즈모드로 전환합니다.')
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print(f'{self.name} : 시즈모드를 해제합니다.')
            self.damage /= 2
            self.seize_mode = False

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{self.name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]')

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중유닛 이동]')
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False # 클로킹 모드(해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print(f'{self.name} : 클로킹 모드를 해제합니다.')
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print(f'{self.name} : 클로킹 모드를 설정합니다.')
            self.clocked - True

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('player : gg') # a good game
    print('[Player] 님이 게임에서 퇴장하셨습니다.')


# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marin
m2 = Marin
m3 = Marin

# 탱크 2기 생성
t1 = Tank
t2 = Tank

# 레이스 1기 생성

w1 = Wraith




