# # # # 애완동물을 소개해 주세요~
# # # animal = "강아지"
# # # name = "연탄이"
# # # age = 4
# # # hobby = "산책"
# # # is_adult = age >= 3

# # # # 주석은 샾으로, 여러 문장은 작은 따옴표 세개 하면
# # # '''
# # # ㅇ
# # # ㅇ
# # # ㅇ
# # # ㅇ

# # # '''

# # # print("우리집 " ,animal + "의 이름은 " + name + "에요")
# # # print(animal, "는 ", age,  "살이며, ", hobby, "을 아주 좋아해요")
# # # print(name + "는 어른일까요?" + str(is_adult))




# # # sentence = '나는 소년입니다.'
# # # print(sentence)
# # # sentence2 = "파이썬은 쉬워요"
# # # print(sentence2)
# # # sentence3 = """
# # # 나는 소년이고, 
# # # 파이썬은 쉬워요
# # # """
# # # print(sentence3)



# # # jumin = "990120-1234567"

# # # print("성별 : "+ jumin) 
# # # print("성별 : " + jumin[7]) 
# # # print("연 : " + jumin[0:2]) # 0부터 2 직전까지
# # # print("월 : "+ jumin[2:4]) # 2부터 4직전까지
# # # print("일 : "+ jumin[4:6]) # 4부터 6직전까지
# # # print("생년월일 : "+ jumin[:6]) # 처음부터 6직전까지
# # # print("뒷번호 : "+ jumin[7:14]) # 7부터 14직전까지
# # # print("뒷번호 : "+ jumin[7:]) # 7부터 끝까지
# # # print("뒷번호 (뒤에서부터) : "+ jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지


# # # python = "Python is Amazing"

# # # print(python.lower())
# # # print(python.upper())
# # # print(python[0].isupper())
# # # print(len(python))
# # # print(python.replace("Python", "Java"))

# # # index = python.index("n")
# # # print(index)
# # # index = python.index("n", index + 1)
# # # print(index)

# # # print(python.find("n"))

# # # print(python.count("n"))

# # # print("a" + "b")
# # # print("a", "b")

# # # print("나는 %d살 입니다." % 20)
# # # print("나는 %s을 좋아해요" % "파이썬")
# # # print("Apple은 %c로 시작해요." % "A")

# # # print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))


# # # print("나는 {}살입니다." .format(2))
# # # print("나는 {}색과 {}색을 좋아해요" .format("빨간", "파란"))
# # # print("나는 {0}색과 {1}색을 좋아해요" .format("빨간", "파란"))
# # # print("나는 {1}색과 {0}색을 좋아해요" .format("빨간", "파란"))

# # # print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20,color = "빨간"))
# # # print("나는 {age}살이며, {color}색을 좋아해요" .format(color = "빨간", age = 20))

# # # age = 20
# # # color = "빨간"
# # # print(f"나는 {age}살이며, {color}색을 좋아해요")

# # # print("백문이 불여일견\n백견이 불여일타")

# # # # 저는 "나도코딩"입니다.
# # # print("저는 나도코딩입니다.")

# # # total = 0
# # # print('숫자를 5번을 입력하여 합계와 평균을 구합니다.')
# # # for i in range(5):
# # #     a = int(input(f'{i+1}번째 숫자를 입력하세요.'))
# # #     total += a
# # # else:
# # #     print(f'합계: {total}, 평균: {total/5}')


# # # a = int(input('2 ~ 9사이의 숫자를 입력하세요.'))
# # # if 2 <= a <= 9:
# # #     for i in range(9):
# # #         print(f'{a} * {i+1} = {a*(i+1)}')
# # # else:
# # #     print('숫자를 다시 입력하세요!! (2 ~ 9사이 숫자입니다)')

# # # class Studunts:
# # #     def __init__(self, name, grade, phone):
# # #         self.name = name
# # #         self.grade = grade
# # #         self.phone = phone

# # #     def introduce(self):
# # #         print(f'안녕하세요. 저는 {self.name}이고, {self.grade}학년 입니다.')
# # #         print(f'제 연락처는 {self.phone}입니다.')

# # #     def grade_up(self):
# # #         self.grade += 1

# # # jima = Studunts('지마', 2, '010-1234-5678')
# # # chamkke = Studunts('참깨', 3, '010-4321-5678')

# # # jima.introduce()
# # # chamkke.introduce()
# # # jima.grade_up()
# # # jima.introduce()

# # # import random
# # # a = [] # 확정된 당첨 로또 번호
# # # b = [] # 내가 선택한 로또 숫자
# # # def playlotto():
# # #     for i in range(6):
# # #         winnum = random.randrange(1,46)
# # #         while winnum in a:
# # #             winnum = random.randrange(1,46)
# # #         a.append(winnum)
    
# # #     c = 0
# # #     while c < 6:
# # #         inpnum = int(input(f'[1 ~ 45]까지의 숫자를 입력하세요.({c + 1}/6번째 숫자)'))
# # #         if inpnum in b:
# # #             print('같은 수를 입력하지 마세요! 다시 숫자를 입력 해 주세요')
# # #             continue
# # #         if inpnum == 0:
# # #             print('나머지 숫자는 자동으로 선택 합니다.')
# # #             for d in range(6-c):
# # #                 num = random.randrange(1,46)
# # #                 while num in b:
# # #                     num = random.randrange(1,46)
# # #                 b.append(num)
# # #             break
# # #         if 0 > inpnum or inpnum > 45:
# # #             print('[1 ~ 45]사이로 숫자를 제대로 입력하세요')
# # #             continue
# # #         b.append(inpnum)
# # #         c += 1
# # #     z = set(a) & set(b)
# # #     if len(z) == 6:
# # #         print()
# # #         print('"축하합니다!!! 1등 당첨!!!!"')
# # #     elif len(z) == 5:
# # #         print()
# # #         print('"2등 당첨!!!"')
# # #     elif len(z) == 4:
# # #         print()
# # #         print('"3등 당첨!"')
# # #     elif len(z) == 3:
# # #         print()
# # #         print('"5천원 당첨이요"')
# # #     else:
# # #         print()
# # #         print('"꽝입니다.ㅎㅎ"')
# # #     print()
# # #     a.sort()
# # #     b.sort()
# # #     print(len(z))

      

# # # playlotto() # 로또 번호 실행기
# # # print('내가 선택한 번호',b) # 내가 선택한 숫자
# # # print('당첨 번호',a) # 당첨 번호

# # # import random
# # # num_range = 20 # 숫자 범위
# # # num_of_answer = 5 # 정답 개수
# # # user_answer = []
# # # num_list = list(range(1, num_range + 1))
# # # prize_greeting = { num_of_answer : '1등!', num_of_answer -1: '2등!', num_of_answer -2: '3등!', num_of_answer -3: '5천원!'}
# # # prize_num = random.sample(num_list, num_of_answer)

# # # while True:
# # #     print('선택 된 수:', user_answer)
# # #     tmp = int(input(f'1~{num_range}의 수 중 하나 입력(0=자동)'))
# # #     if 1 <= num_range:
# # #         if tmp not in user_answer:
# # #             user_answer.append(tmp)
# # #             num_list.remove(tmp)
# # #         else:
# # #             print('이미 선택한 번호입니다.')
# # #             continue
# # #     elif tmp == 0:
# # #         for i in random.sample(num_list, num_of_answer - len(user_answer)):
# # #             user_answer.append(i)
# # #     else:
# # #         print('유효하지 않은 입력입니다.')
# # #         continue
# # #     if num_of_answer == len(user_answer):
# # #         print('입력완료!', user_answer)
# # #         break

# # # print('정답체크!', prize_num)
# # # cnt = len(set(prize_num)&(set(user_answer)))

# # # if cnt in prize_greeting.keys():
# # #     print(prize_greeting[cnt])
# # # else:
# # #     print('낙첨되었습니다.')

# # # for i in range(4):
# # #     print('*')


# # # n = 4
# # # for r in range(1, n + 1):
# # #     for c in range(1, n + 1):
# # #         print('*', end="") # 기본 줄바꿈 삭제
# # #     print()

# # # for r in range(1, n + 1):
# # #     for c in range(1, r + 1):
# # #         print('*',end = "") 
# # #     print()

# # # for r in range(1, n + 1):
# # #     for c in range(1, r + 1):
# # #         print('*',end = "") 
# # #     print()

# # # n = 4
# # # for r in range(1, n +1):
# # #     for c in range(1, n-r + 1):
# # #         print('a', end = "")
# # #     for c in range(1, r*2-1 + 1):
# # #         print('*', end = '')
# # #     print()

# # # for lv in range(2, 10):
# # #     # 단 시작
# # #     for step in range(1, 10, 3):
# # #         for c in range(3):
# # #             print(f'{lv} X {step + c} = {lv * (step + c)}   ', end='')
# # #         print()
# # #     # 단 종료

# # #     print()


# # # class Engin:
# # #     def __init__(self, e_type):
# # #         self.e_type = e_type # privet 실행 가능 self.__e_type = e_type
# # #         print(f'{self.e_type}엔진 탑재')

# # # auto = Engin('자동')
# # # print(auto.e_type)
# # # auto.e_type = '수동' # 외부에서 변수에 접근하여 조작 가능
# # # print(auto.e_type)

# # # class Engine:
# # #     def __init__(self, e_type):
# # #         self.__e_type = e_type
# # #         print(f'{self.__e_type}엔진 탑재')

# # #     def get_type(self):
# # #         return self.__e_type

# # #     def set_type(self, e_type):
# # #         if e_type in ['수동', '자동', 'auto', 'manual']:
# # #             self.__e_type = e_type
# # #         else:
# # #             print('지정할 수 없는 타입입니다.')

# # # auto = Engine('자동')
# # # print(auto.get_type())
# # # auto.set_type('수동')
# # # auto.set_type('엄복동')
# # # print(auto.get_type())

# # # 직접 조작의 편리성과 캡슐화의 보안성을 합친 property
# # # class Engine:
# # #     def __init__(self, e_type):
# # #         self.__e_type = e_type
# # #         print(f'{self.__e_type}엔진 탑재')

# # #     @property
# # #     def e_type(self):
# # #         return self.__e_type

# # #     @e_type.setter
# # #     def e_type(self, e_type):
# # #         if e_type in ['수동', '자동', 'auto', 'manual']:
# # #             self.__e_type = e_type
# # #         else:
# # #             print('지정할 수 없는 타입입니다.')


# # # auto = Engine('자동')
# # # # print(auto.e_type)
# # # auto.e_type = '수동'
# # # auto.e_type = '엄복동'
# # # # print(auto.e_type)

# # # # print()

# # # class Tier:
# # #     def __init__(self, size):
# # #         self.__t_size = size
# # #         print(f'{self.__t_size}인치 타이어 탑재')

# # #     @property
# # #     def t_size(self):
# # #         return self.__t_size

# # #     @t_size.setter
# # #     def t_size(self, size):
# # #         if 14 <= size <= 18:
# # #             self.__t_size = size
# # #         else:
# # #             print('14~18인치 사이의 값만 지정')

# # # wheel = Tier(15)
# # # # print(wheel.t_size)
# # # wheel.t_size = 17
# # # wheel.t_size = 20
# # # # print(wheel.t_size)

# # # # print()

# # # class OptionBronze:
# # #     def __init__(self):
# # #         self.airbag()
# # #         self.aircon()
    
# # #     def airbag(self):
# # #         print('전좌석 에어백')

# # #     def aircon(self):
# # #         print('수동 에어컨')

# # # class OptionSilver(OptionBronze):
# # #     def __init__(self):
# # #         self.airbag()
# # #         self.aircon()
# # #         self.heat_wire()
    
# # #     def aircon(self):
# # #         print('자동 에어컨') # class 오버라이딩

# # #     def heat_wire(self):
# # #         print('핸들+앞좌석 열선시트')

# # # class OptionGold(OptionSilver):
# # #     def __init__(self):
# # #         self.airbag()
# # #         self.aircon()
# # #         self.heat_wire()
# # #         self.sunroof()
    
# # #     def heat_wire(self):
# # #         print('핸들+전좌석 열선시트') # 오버라이딩: 재 정의 하는 것

# # #     def sunroof(self):
# # #         print('썬루프')


# # # class Car(Engine, Tier):
# # #     __rel_list = []
# # #     op_type = {'브론즈' : OptionBronze, '실버' : OptionSilver, '골드' : OptionGold}

# # #     def __init__(self, e_type, op_type, tier_size=15):
# # #         print('Car Released'.center(20, '='))
# # #         Engine.__init__(self, e_type)
# # #         Tier.__init__(self, e_type)
# # #         print('=Option List'.ljust(20,'='))
# # #         self.option = self.op_type[op_type]()
# # #         print('Thank you!=\n'.rjust(20,'='))
# # #         self.__rel_list.append(self)

# # #     def release_report(self):
# # #         print(f'현재까지 {len(self.__rel_list)}대의 차량이 출고 됨')


# # # jima = Car('수동', '브론즈')
# # # chamkke = Car('자동', '골드', 18)
# # # print(jima.e_type)
# # # print(jima.t_size)
# # # jima.t_size = 20
# # # print(jima.t_size)
# # # jima.release_report()

# # # students = [1,2,3,4,5]
# # # s = []
# # # print(students)
# # # for i in students:
# # #     if 1 <= i <= 4:
# # #         s.append(i+100)

# # # print(s)

# # # students = [1,2,3,4,5]
# # # print(students)
# # # students = [i+100 for i in students]
# # # print(students)

# # # students = ['Iron man', 'Thor', 'i am groot']
# # # students = [len(i) for i in students]
# # # print(students)

# # # a = ['red apple', 'nike shose']

# # # def open_account():
# # #     print('새로운 계좌가 생성되었습니다.')

# # # def deposit(balance, money): #입금
# # #     print(f'입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.')
# # #     return balance + money

# # # def withdraw(balance, money): #출금
# # #     if balance - money < 0:
# # #         print('잔액이 부족합니다.')
# # #     else:
# # #         print(f'출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.')
# # #     return balance - money

# # # def withdraw_night(balance, money): #저녁에 출금, 수수료
# # #     commition = 100
# # #     if balance - money - commition < 0:
# # #         print('잔액이 부족합니다.')
# # #     else:
# # #         print(f'수수료는 {commition}원이며 {money}원 출금이 완료되었습니다. 잔액은 {balance - money - commition}원 입니다.')
# # #     return commition, balance - money - commition

# # # balance =  0
# # # balance = deposit(balance, 1000)
# # # # print(balance)
# # # balance = deposit(balance, 1000)
# # # commition, balance = withdraw_night(balance, 500)
# # # balance = deposit(balance, 1000)
# # # withdraw(balance, 2000)


# # # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# # #     print(f'이름 : {name}\t 나이 : {age}\t', end=' ')
# # #     print(lang1, lang2, lang3, lang4, lang5)

# # # profile('유재석', 20, 'Python', 'Jave', 'C', 'C++', 'C#')
# # # profile('김태호', 25, 'Kotlin', 'Swift', '', '', '')


# # # def profile(name, age, *language):
# # #     print(f'이름 : {name}\t나이 : {age}\t', end=' ')
# # #     for lang in language:
# # #         print(lang, end=' ')
# # #     print()

# # # profile('유재석', 20, 'Python', 'Jave', 'C', 'C++', 'C#', 'JavaScript')
# # # profile('김태호', 25, 'Kotlin', 'Swift')

# # # gun = 10
# # # def checkpoint(soldiers): # 경계근무
# # #     global gun #전역 공간에 있는 gun 사용
# # #     # gun #  global 없이 일반 변수 gun 사용하면 오류가 뜸
# # #     gun = gun - soldiers
# # #     print(f'[함수 내] 남은 총 : {gun}')

# # # def checkpoint_ret(gun, soldiers):
# # #     gun = gun - soldiers
# # #     print(f'[함수 내] 남은 총 : {gun}')
# # #     return gun


# # # print(f'전체 총 : {gun}')
# # # # checkpoint(2) # 2명이 경계 근무 나감
# # # gun = checkpoint_ret(gun,2)
# # # print(f'남은 총 : {gun}')

# # #  # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# # # print('{0: >10}'.format(500))
# # # # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# # # print('{0: >+10}'.format(500))
# # # print('{0: >10}'.format(-500))
# # # # 왼쪽 정렬하고, 빈칸으로 _로 채움
# # # print('{0:-<10}'.format(500))
# # # # 3자리마다 콤마를 찍어주기
# # # print('{0:,}'.format(50000000000))
# # # # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# # # print('{0:+,}'.format(50000000000))
# # # print('{0:+,}'.format(-50000000000))
# # # # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # # # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# # # print('{0:^<+30,}'.format(50000000000))
# # # # 소수점 출력
# # # print('{0:f}'.format(5/3))
# # # # 소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
# # # print('{0:.2f}'.format(5/3))

# # # score_file = open('score.txt', 'w', encoding='utf8')
# # # print('수학 : 0', file=score_file)
# # # print('영어 : 50', file=score_file)
# # # score_file.close()

# # # score_file = open('score.txt','a', encoding='utf8')
# # # score_file.write('과학 : 80')
# # # score_file.write('\n코딩 : 100')
# # # score_file.close()

# # # score_file = open('score.txt', 'r', encoding='utf8')
# # # print(score_file.read())
# # # score_file.close()

# # # score_file = open('score.txt', 'r', encoding='utf8')
# # # print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# # # print(score_file.readline())
# # # print(score_file.readline())
# # # print(score_file.readline())
# # # score_file.close()

# # # score_file = open('score.txt', 'r', encoding='utf8')
# # # while True:
# # #     line = score_file.readline()
# # #     if not line:
# # #         break
# # #     print(line)
# # # score_file.close()

# # # score_file = open('score.txt', 'r', encoding='utf8')
# # # lines = score_file.readlines() # list 형태로 저장
# # # for line in lines:
# # #     print(line)
# # # score_file.close()

# # # import pickle
# # # # profile_file = open('profile.pickle', 'wb')
# # # # profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
# # # # print(profile)
# # # # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # # # profile_file.close()

# # # profile_file = open('profile.pickle', 'rb')
# # # profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# # # print(profile)
# # # profile_file.close()

# # # import pickle

# # # with open('profile.pickle', 'rb') as profile_file:
# # #     print(pickle.load(profile_file))

# # # with open('study.txt', 'w', encoding='utf8') as study_file:
# # #     study_file.write('파이썬을 열심히 공부하고 있어요')

# # # with open('study.txt', 'r', encoding='utf8') as study_file:
# # #     print(study_file.read())

# # # Class 강의

# # # # 마린 : 공격 유닛, 군인. 총을 쓸 수 있음
# # # name = '마린' # 유닛의 이름
# # # hp = 40 # 유닛의 체력
# # # damage = 5 # 유닛의 공격력

# # # print(f'{name} 유닛이 생성되었습니다.')
# # # print(f'체력{hp}, 공격력{damage}\n')

# # # # 탱크 : 공격 유닛, 탱크, 포를 쓸 수 있는데, 일반 모드 / 시즈 모드
# # # tank_name = '시즈탱크' # 유닛의 이름
# # # tank_hp = 150 # 유닛의 체력
# # # tank_damage = 35

# # # print(f'{tank_name} 유닛이 생성되었습니다.')
# # # print(f'체력{tank_hp}, 공격력{tank_damage}\n')

# # # def attack(name, location, damage):
# # #     print(f'{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]')

# # # attack(name,'1시', damage)
# # # attack(tank_name,'1시', tank_damage)


# # # class Unit: # 클래스는 붕어빵 틀과 같음. 클래스를 이용해서 클래스 안에 정의되어 있는 것들을 통해 객체를 생성 할 수 있음.
# # #     def __init__(self, name, hp, damage):
# # #         self.name = name
# # #         self.hp = hp
# # #         self.damage = damage
# # #         print(f'{self.name} 유닛이 생성되었습니다.')
# # #         print(f'체력{self.hp}, 공격력{self.damage}\n')


# # # marin1 = Unit('마린', 40, 5)
# # # marin2 = Unit('마린', 40, 5)
# # # tank = Unit('시즈탱크', 150, 35)

# # # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)

# # # wraith1 = Unit('레이스', 80, 5)
# # # print(f'유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}')

# # # # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# # # wraith2 = Unit('빼앗은 레이스', 80, 5)
# # # wraith2.clocking = True

# # # if wraith2.clocking == True:
# # #     print(f'{wraith2.name}는 현재 클로킹 상태입니다.')

# # # 일반 유닛
# import imp
# from tkinter import N

# from travel import thailand
# import travel


# class Unit: 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def monve(self, location):
#         print('[지상 유닛 이동]')
#         print(f'{self.name} : {location} 방향으로 이동 [속도 : {self.speed}]')

# # # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(f'{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')


#     def damaged(self, damage):
#         print(f'{self.name} : {damage} 데미지를 입었습니다.')
#         self.hp -= damage
#         print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
#         if self.hp <= 0:
#             print(f'{self.name} : 파괴되었습니다.')


# # # #파이어뱃 : 공격 유닛, 화염방사기
# # # firebat1 = AttackUnit('파이어뱃', 50, 16)
# # # firebat1.attack('5시')

# # # firebat1.damaged(25)
# # # firebat1.damaged(25)

# # # 드랍쉽 : 공중 유닛, 수송기 마린 / 파이어뱃 / 탱크 등을 수송. 공경 X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f'{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]')

# # # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print('[공중 유닛 이동]')
#         self.fly(self.name, location)

# # # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# # # valkyrie = FlyableAttackUnit('발키리', 200 ,6, 5)
# # # valkyrie.fly(valkyrie.name, '3시')

# # # 벌쳐 : 지상 유닛, 기동성이 좋음
# # vulture = AttackUnit('벌쳐', 80, 10, 20)

# # # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# # battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

# # vulture.monve('11시')
# # # battlecruiser.fly(battlecruiser.name, '9시')
# # battlecruiser.move('9시')

# # # 건물
# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         #Unit.__init__(self, name, hp, location):
# #         super().__init__(name, hp, 0) # supte를 쓸 때 super옆에 괄호 붙이고 변수에 self 뺌
# #         self.location = location

# # try:
# #     print('나누기 전용 계산기입니다.')
# #     num1 = int(input('첫 번째 숫자를 입력하세요 : '))
# #     num2 = int(input('두 번째 숫자를 입력하세요 : '))
# #     print(f'{num1} / {num2} = {num1/num2}')
# # except ValueError:
# #     print('에러! 잘못된 값을 입력하였습니다.')

# # import theater_modul
# # theater_modul.price(3)
# # theater_modul.price_morning(4)
# # theater_modul.price_soldier(6)

# # import theater_modul as mv # as 뒤에 별명을 붙일 수 있음
# # mv.price_soldier(1)
# # mv.price_morning(2)

# # from theater_modul import *
# # price(3)
# # price_morning(4)
# # price_soldier(5)

# # from theater_modul import price, price_morning
# # price_morning(1)
# # price(1)

# # from theater_modul import price_soldier as price
# # price(5)

# # import travel.thailand
# # trip_to = travel.thailand.ThailandPackage()
# # trip_to.detail()

# # from travel.thailand import ThailandPackage
# # trip_to = ThailandPackage()
# # trip_to.detail()

# # from travel import vietnam
# # trip_to = vietnam.VietnamdPackage()
# # trip_to.detail()

# # from travel import *
# # # trip_to = vietnam.VietnamdPackage()
# # # trip_to.detail()

# # import inspect
# # import random
# # print(inspect.getfile(random))
# # print(inspect.getfile(thailand))

import numpy as np
np_arr = np.array(range(5))
print(np_arr)
print(type(np_arr))