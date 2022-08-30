class Knight:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 20
        self.attack_type = '근접'
        self.attack = 30
        self.armor = 10
        self.potion_cnt = 3
        print('기사 캐릭터 생성 완료!')

    def under_attack(self, attacker):
        # 공격타입이 마법일 경우엔 20% 데미지 가중
        if attacker.attack_type =='마법':
            multiple = 1.2
        else:
            multiple = 1
        # 공격력 * 가중치 - 방어력
        damage = attacker.attack * multiple - self.armor
        self.hp -= damage
        print(f'{self.name}: {attacker.name}님의 공격({damage})에 의해 HP[{self.hp}]')
        # 체력이 0이 된 경우, 사망 메시지 출력
        if self.hp <= 0:
            print(f'{self.name}님이 {attacker.name}님에 의해 사망하였습니다.')

    def attack_to(self, target):
        # 공격 대상의 체력이 0 이상일 때만 실행
        if target.hp > 0:
            print(f'{self.name}님이 {target.name}님을 공격합니다.')
            # 공격 대상의 피격 메소드 호출
            target.under_attack(self)
    
    def triple_attack(self, target):
        # mp가 20 이상일 때만 사용 가능
        if self.mp >= 20:
            self.mp -= 20
            print(f'{self.name}님이 {target.name}님을 3회 공격합니다.')
            # 공격 대상의 under_attack메소드 3회 호출
            for i in range(3):
                target.under_attack(self)

    def use_potion(self):
        if self.potion_cnt > 0:
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
            print(f'{self.name}님 포션 1개 사용합니다.\n남은 포션 {self.potion_cnt - 1}개 HP[{self.hp}]')
            self.potion_cnt -= 1
        else:
            print('포션이 남아있지 않습니다.')

k1 = Knight('길동')
k2 = Knight('철수')
print()

k1.attack_to(k2)
print()
k1.attack_to(k2)
print()
k2.attack_to(k1)
print()
k2.attack_to(k1)
print()
k1.use_potion()
print()
k1.use_potion()
print()
k1.use_potion()
print()
k1.use_potion()
print()
k1.triple_attack(k2)
print()