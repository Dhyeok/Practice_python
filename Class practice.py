# class Engin:
#     def __init__(self, e_type):
#         self.e_type = e_type # privet 실행 가능 self.__e_type = e_type
#         print(f'{self.e_type}엔진 탑재')

# auto = Engin('자동')
# print(auto.e_type)
# auto.e_type = '수동' # 외부에서 변수에 접근하여 조작 가능
# print(auto.e_type)

# class Engine:
#     def __init__(self, e_type):
#         self.__e_type = e_type
#         print(f'{self.__e_type}엔진 탑재')

#     def get_type(self):
#         return self.__e_type

#     def set_type(self, e_type):
#         if e_type in ['수동', '자동', 'auto', 'manual']:
#             self.__e_type = e_type
#         else:
#             print('지정할 수 없는 타입입니다.')

# auto = Engine('자동')
# print(auto.get_type())
# auto.set_type('수동')
# auto.set_type('엄복동')
# print(auto.get_type())

# 직접 조작의 편리성과 캡슐화의 보안성을 합친 property
class Engine:
    def __init__(self, e_type):
        self.__e_type = e_type
        print(f'{self.__e_type}엔진 탑재')

    @property
    def e_type(self):
        return self.__e_type

    @e_type.setter
    def e_type(self, e_type):
        if e_type in ['수동', '자동', 'auto', 'manual']:
            self.__e_type = e_type
        else:
            print('지정할 수 없는 타입입니다.')


auto = Engine('자동')
# print(auto.e_type)
auto.e_type = '수동'
auto.e_type = '엄복동'
# print(auto.e_type)

# print()

class Tier:
    def __init__(self, size):
        self.__t_size = size
        print(f'{self.__t_size}인치 타이어 탑재')

    @property
    def t_size(self):
        return self.__t_size

    @t_size.setter
    def t_size(self, size):
        if 14 <= size <= 18:
            self.__t_size = size
        else:
            print('14~18인치 사이의 값만 지정')

wheel = Tier(15)
# print(wheel.t_size)
wheel.t_size = 17
wheel.t_size = 20
# print(wheel.t_size)

# print()

class OptionBronze:
    def __init__(self):
        self.airbag()
        self.aircon()
    
    def airbag(self):
        print('전좌석 에어백')

    def aircon(self):
        print('수동 에어컨')

class OptionSilver(OptionBronze):
    def __init__(self):
        self.airbag()
        self.aircon()
        self.heat_wire()
    
    def aircon(self):
        print('자동 에어컨') # class 오버라이딩

    def heat_wire(self):
        print('핸들+앞좌석 열선시트')

class OptionGold(OptionSilver):
    def __init__(self):
        self.airbag()
        self.aircon()
        self.heat_wire()
        self.sunroof()
    
    def heat_wire(self):
        print('핸들+전좌석 열선시트') # 오버라이딩: 재 정의 하는 것

    def sunroof(self):
        print('썬루프')


class Car(Engine, Tier):
    __rel_list = []
    op_type = {'브론즈' : OptionBronze, '실버' : OptionSilver, '골드' : OptionGold}

    def __init__(self, e_type, op_type, tier_size=15):
        print('Car Released'.center(20, '='))
        Engine.__init__(self, e_type)
        Tier.__init__(self, e_type)
        print('=Option List'.ljust(20,'='))
        self.option = self.op_type[op_type]()
        print('Thank you!=\n'.rjust(20,'='))
        self.__rel_list.append(self)

    def release_report(self):
        print(f'현재까지 {len(self.__rel_list)}대의 차량이 출고 됨')


jima = Car('수동', '브론즈')
chamkke = Car('자동', '골드', 18)
print(jima.e_type)
print(jima.t_size)
jima.t_size = 20
print(jima.t_size)
jima.release_report()