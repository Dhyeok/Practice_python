# print(abs(-5)) #abs 는 절대값 구하는 함수
# print(pow(4 , 2)) #pow 는 제곱 하는 함수
# print(max (5, 12)) #max는 조건중 최대 값
# print(min(5 , 12)) #min은 조건중 최소 값
# print(round(3.14)) #round는 반올림 값
# print(round(4.99))

# import imp
# from math import * #파이썬에서 제공하는 수학 함수 모두 사용
# print(floor(4.99)) #소수점 내림
# print(ceil(3.14)) #소수점 올림
# print(sqrt(16)) # 제곱근


# #랜덤함수

# from random import *
# print(random()) # 0.0이상 1.0 미만의 랜덤 값을 생성 
# print(random() * 10) # 0.0 ~ 10.0 미만의 랜덥 값 생성

# print(int(random () * 10)) #0 ~ 10 미만의 랜덤 값 생성 int = 소수점이하 버려주는 함수
# print(int(random () * 10)) #0 ~ 10 미만의 랜덤 값 생성
# print(int(random () * 10)) #0 ~ 10 미만의 랜덤 값 생성

# print(int(random() * 10) + 1) # 1 ~ 10 이하의 랜덥 값 생성



# #로또 예재

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 랜덤 값 생성

# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성
# print(randrange(1,46)) # 1 ~ 46미만의 랜덤 값 생성

# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성
# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성
# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성
# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성
# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성
# print(randint(1 , 45)) # 1 ~ 45이하의 랜덤 값 생성

# for n in range(1, 31, 10):
#     print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')

# person = ('123')
# for k in person:
#     print(k)

# from turtle import window_height


# max = 25
# weight = 0
# item = 3

# while weight + item <= max:
#     weight += item
#     print('짐을 추가합니다')
# print(f'총무게는 {weight} 입니다.')


# i = 3
# while i <= 5:
#     print(i)
#     i += 1

# drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
# for x in drama:
#     if x == '시즌3':
#         print('재비없대, 건너뛰자')
#         continue
#     print(f'{x} 시청')

# for x in range(10):
#     if x%2 ==1:
#         continue
#     print(x)

# products = ['JOA-2020', 'JOA-2020=1', 'SIRO-2021', 'SIRO-2022']
# recall = []
# for p in products:
#     if p.startswith('SIRO'):
#         recall.append(p)


# print(recall)

# for x in range(10):
#     print('팔 벌려 뛰기 해')

# for v in range(10):
#     print(f'팔 벌려 뛰기 {v}회')

# my_list = [1, 2, 3, 4, 5]
# new_list = [str(x) + '번째' for x in my_list ]

# print(new_list)

# products = ['JOA-2020', 'JOA-2020=1', 'SIRO-2021', 'SIRO-2022']
# recall = [x for x in products if x.startswith('SIRO')]
# prod_se =   [x + 'SE' for x in products]
# prod_new = [x +'(최신형)' for x in products if x.endswith('2022')]

# print(prod_new)

# my_list =   ['korea', 'english', 'france', 'japan', ]
# new_list = [x.upper() for x in my_list if 'a' in x]

# print(new_list)

# def show_price():
#     print('감성 컷트 가격은 15,000원 입니다.')

# customer1 = '나장발'
# print(f'{customer1} 고객님')
# show_price()

# customer2 = '나수염'
# print(f'{customer2} 고객님')
# show_price()

# def my_function():
#     print('새로운 \n함수를 \n만들었어요')


# my_function()


# def show_price(customer):
#     print(f'사랑하는 {customer} 고객님')
#     print('감성 컷트 가격은 15,000원 입니다.')

# customer1 = '나장발'
# show_price(customer1)

# customer2 = '나수염'
# show_price(customer2)

# def get_price(is_vip):
#     if is_vip == True:
#         return 10000
#     else:
#         return 15000

# price = get_price(True)

# print(f'커트가격은 {price}원 입니다.')


# def get_price(is_vip=False):
#     if is_vip == True:
#         return 10000
#     else:
#         return 15000

# price = get_price()

# print(f'커트가격은 {price}원 입니다.')


# from tracemalloc import take_snapshot


# def order(shot=2, size='Regular', takout=True):
#     print(f'아메리카노 {size}사이즈 {shot}샷')
#     if takout:
#         print('포장주문이 완료되었습니다.')
#     else:
#         print('주문이 완료되었습니다.')

# order('Regular', takout=True)

# def visit(today, *customers):
#     print(today)
#     for customer in customers:
#         print(customer)

# visit('2022년 6월 10일', '나장발', '나수염')

# print('팔벌려뛰기 1해')

# for x in range(1,11):
#     print(f'팔벌려 뛰기 {x}회 해')

# message = '나는야 전역변수'

# print(message)

# def no_secret():
#     global message
#     message = '오 진짜 전역변수!!'

# no_secret()
# print(message)

# name = input('예약자분 성함이 어떻게 되나요?')
# print(name)

# num = int(input('총 몇분이세요?'))
# if num > 4:
#     print('죄송합니다. 저희 식당은 최대 4명까지 입장이 가능합니다.')
# else:
#     print('이쪽 테이블에 앉으세요^^')

# print(num)

# dream = input('당신의 꿈은 무엇인가요?')
# print(f'제꿈은 {dream}입니다.')


# f = open('list.txt', 'w' , encoding='utf8')
# f.write('김xx\n')
# f.write('정xx\n')
# f.write('허xx\n')
# f.close()


# f = open('list.txt', 'r', encoding='utf8')
# contents = f.read()
# print(contents)
# f.close

# f = open('list.txt', 'r', encoding='utf8')
# for line in f:
#     print(line, end='')
# f.close()


# with open('list.txt', 'r', encoding = 'utf8') as f:
#     contents = f.read()
#     print(contents)

# class BlackBox:
#     pass

# b1 = BlackBox()
# b1.name = '까망이'
# print(b1.name)
# print(isinstance(b1, BlackBox))

# b2 = BlackBox()
# print(b2.name)

# class BlackBox:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# b1 = BlackBox('까망이', 200000)
# b1.nickname = '1호'
# print(b1.name, b1.price, b1.nickname)

# b2 = BlackBox('햐양이', 100000)
# print(b2.name, b2.price,)

# class BlackBox:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def set_travel_mode(self, min):
#         print(str(min) + '분 동안 여행모드 ON')

# b1 = BlackBox('까망이', 200000)
# b1.set_travel_mode(20)

# class Student:
#     def introduce(self, name, age):
#         print(f'제 이름은 {name} 이고 나이는 {age}살 입니다. ')

# student1 = Student()
# student1.introduce('최병관','30')

# student2 = Student()
# student2.introduce('민종성', '30')

# class BlackBox:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def set_travel_mode(self, min):
#         print(f'{self.name} {min}분 동안 여행모드 ON')

# b1 = BlackBox('까망이', 200000)
# b2 = BlackBox('하양이', 100000)

# BlackBox.set_travel_mode(b1,20)



# class BlackBox: #부모 클래스
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class TravelBlackBox(BlackBox): #자식 클래스
#     def set_travel_mode(self, min):
#         print(f'{self.name} {min}분 동안 여행모드 ON')


# b1 = BlackBox('까망이', 200000)
# b2 = TravelBlackBox('하양이', 100000)

# print(b2.name, b2.price)
# b2.set_travel_mode(20)

# class MailSender:
#     def send(self):
#         print('메일발송')



# class VideoMaker:
#     def make(self):
#         print('추억용 여행 영상 제작')


# class BlackBox: #부모 클래스
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class TravelBlackBox(BlackBox, VideoMaker, MailSender): #자식 클래스
#     def __init__(self, name, price, sd):
#         super().__init__(name, price) # = BlackBox.__init__(self, name, price)
#         self.sd = sd
    
#     def set_travel_mode(self, min):
#         print(str(min) + '분 동안 여행모드 ON')



# class AdvancedTravelBlackBox(TravelBlackBox):
#     def set_travel_mode(self, min):
#         print(str(min) + '분 동안 여행모드 ON')
#         self.make()
#         self.send()


# b1 = AdvancedTravelBlackBox('하양이', 100000, 64)
# b1.set_travel_mode(20)


# num1 = 3
# num2 = '9'


# try:
#     result = num1 / num2
#     print(f'연산 결과는 {result} 입니다.')

# except ZeroDivisionError:
#     print('0 으로 나눌 수 없어요')

# except TypeError:
#     print('값의 형태가 이상해요')

# except Exception as err:
#     print('에러가 발생했어요:', err)

# else:
#     print('정상 동작했어요')

# finally:
#     print('수행 종료')

# import goodjob
# goodjob.say()


# from goodjob import say

# import random
# my_list = ['가위', '바위', '보']
# print(random.choice(my_list))

# import nadocoding.goodjob
# nadocoding.goodjob.say()

# from nadocoding import goodbye
# goodbye.bye()

# x = int(input('점수를 입력하세요'))
# if x > 80:
#     print('A')
# elif x <= 80 and x > 60 :
#     print('B')
# elif x <= 60 and x > 50 :
#     print('C')
# elif x <= 50 and x > 40 :
#     print('D')
# else :
#     print('F')

# print('바밤바는')
# print('바밤바')
# print('바빔')

# print('나는 %d살입니다.' % 20)
# print('나는 %s을 좋아해요' % 'Python')
# print('Apple은 %c로 시작해요' % 'A')

# print(0o455) #8진수
# print(0xaf23) #16진수
# print(0b10011101) #2진수



# print('비참한 삶에서 벗어날 수 있는 방법이 두 가지 있다.\n그것은 \'음악\'과 \'고양이\'이다.\n- 알버트 슈바이처')
 

# f_str = '식:{0}={1}, 타입:{2}'
# res_1, res_2 = 2+3, 10-2.0
# exp_1, exp_2 = '2+3', '10-2.0'
# type_1 = str(type(res_1))[8:-2] #class 'int'
# type_2 = str(type(res_2))[8:-2] #class 'float'

# print(f_str.format(exp_1, res_1, type_1))
# print(f_str.format(exp_2, res_2, type_2))


# print(type_1)

# print('안녕하세요. 당신의 BMI를 구해 드립니다.')

# weiinput = int(input('몸무게를 입력 해 주세요'))
# print(weiinput)

# heiinput = int(input('키를 입력 해 주세요.')) / 100
# print(heiinput)

# bmi = weiinput / (heiinput ** 2)

# print(f'당신의 BMI 수치는 {bmi} 입니다.')




# a = 173
# b = 60
# c = a / (b ** 2)

# print(c)



# a = '880917 -1234567'
# print(f'19{a[0:2]}년 {a[2:4]}월 {a[4:6]}일')

# a = int(input('첫번째 수'))
# b = int(input('두번째 수'))

# if a < b:
#     a, b = b, a

# if a - b >= 20:
#     print('편차 큼')

# singnum = int(input('노래 검색기 입니다. 5자리 숫자를 입력해 주세요'))

# if singnum == 89245:
#     print('아로하(조정석)')
# elif singnum == 99968:
#     print('Baby(블루)')
# elif singnum == 91936:
#     print('흔들리는꽃들속에서네샴푸향이느껴진거야(장범준)')
# else:
#     print('아무노래(지코)')

# name = ['김똘똘', '박영재', '홍일등', '강천재', '한전교']
# score = [80, 67, 90, 50, 78]
# for i in range(5):
#     if score[i] >= 90:
#         grade = 'A'
#     elif 90 > score[i] >= 80:
#         grade = 'B'
#     elif 80> score[i] >= 70:
#         grade = 'C'
#     elif 70 > score[i] >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     print(f'{name[i]} 학생의 점수는 {score[i]}점이고 등급은 {grade}입니다.')
    



# scores = [['김똘똘', 80],['박영재', 67], ['홍일등', 90], ['강천재', 50], ['한전교', 78]]

# for i in scores:
#     print(i[0], i[1])

# 
# for idx, value in enumerate(number):
#     if value == key:
#         print(f'{key}은 {idx+1}번째 위치에 있습니다.')
#         break


# print(list(enumerate(number)))

# score = int(input('점수를 입력하세요'))
# while 0 <= score <= 100:
#     if score >= 90:
#         print('합격입니다.')
#     elif score >= 80:
#         print('재시험 응시!')
#     else:
#         print('불합격입니다...')
#     score = int(input())

    
# while True:
#     score = int(input('점수를 입력하세요'))
#     if score < 0 or score > 100:
#         break
#     if score >= 90:
#         print('합격입니다.')
#     elif score >= 80:
#         print('재시험 응시!')
#     else:
#         print('불합격입니다...')

# a = int(input('숫자를 입력하세요.'))

# for i in range(1,a+1):
#     print(i)

# nums = [8, 9, 13, 14, 2, 5, 60, 32, 33]
# odd = 0
# even = 0
# for i in nums:
#     if i % 2 == 1:
#         odd += 1
#     else:
#         even += 1

# print('홀수:', odd)
# print('짝수:', even)

# nums = []
# f_nums = []
# while True:
#     a = int(input('정수를 입력하세요.'))
#     if a == 0:
#         break
#     else:
#         nums.append(a)
#     for b in nums:
#         if b % 4 == 0:
#             f_nums.append(b)
#     print(len(f_nums))

# even_4 = 0
# while True:
#     tmp = int(input('입력 :'))
#     if tmp == 0:
#         even_4 += 1
# print('4의 배수:', even_4)


# total = 0
# for i in range(5):
#     tmp = int(input(f'{i+1}번째 수 입력'))
#     total += tmp
# else:
#     print('합계:', total)
#     print('평균:', total/5)


# a = int(input('단 수 입력 : '))
# for b in range(1, 10):
#     print(f'{a} * {b} = {a*b}')

# target = int(input('몇 번째 소수를 구할까요: '))
# cnt_p = 0
# number = 2
# while True:
#     for divisor in range(2, int(number/2)+1):
#         if number % divisor == 0:
#             break
#     else:
#         cnt_p += 1
#     if cnt_p == target:
#         print(f'{target}번째 소수는 {number}입니다.')
#         break
#     else:
#         number += 1

# n = 144
# x = 1
# for i in range(10):
#     x = (x + n / x) / 2

# print(x)

# import math
# print(math.sqrt(144))

# val = int(input('정수 입력: '))
# sq_val = val * val
# print(sq_val)

# def func():
#     val = int(input('정수 입력: '))
#     sq_val = val * val
#     print(sq_val)

# func()

# def add(a,b):
#     return a + b

# print(add(3,4))

# total = 0
# for i in range(3):
#     a = int(input('점수를 입력하세요(세번 입력합니다.)'))
#     if a < 0:
#         print('0보다 큰 숫자를 입력하세요! 다시 입력 하세요')
#     else:
#         total += a
# avr = total/3
# if avr >= 80:
#     print(f'3 과목 점수 평균 : {avr}')
#     print('합격 입니다. ^^')
# else:
#     print(f'3 과목 점수 평균 : {avr}')
#     print('불합격 입니다. 공부 더 하세요!')



# def val_chk(scr1, scr2, scr3):
#     #셋 중 가장 작은 값이 0 이상이면 true를 반환
#     #그렇지 않으면(0 미만이면) false를 반환
#     return min(scr1, scr2, scr3) >= 0

# def pass_n_fail(score):
#     if score >= 80:
#         print('합격입니다.')
#         print('축하합니다.')
#     else:
#         print('불합격입니다.')
#     print('수고하셨습니다.')

# def avg_score(scr1, scr2, scr3):
#     # val_chk의 결과가 true일 때만 실행
#     if val_chk(scr1, scr2, scr3):
#         score = (scr1 + scr2 + scr3) / 3
#         pass_n_fail(score)

# def weight_score(scr1, scr2, scr3):
#     # val_chk의 결과가 true일 때만 실행
#     if val_chk(scr1, scr2, scr3):
#         score = scr1 * 0.3 + scr2 * 0.4 + scr3 * 0.3
#         pass_n_fail(score)


# avg_score(90, 90, 90)
# weight_score(60, 70, 50)

# def rep_prt(str,num):
#     for i in range(num):
#         print(str)

# rep_prt('안녕하세요' , 2)
# rep_prt('하이룽' , 3)

# def chknnum(a, b):
#     if max(a , b) < 0:
#         return
#     elif abs(a) > abs(b):
#         print(abs(a) - abs(b))
#     else:
#         print(abs(a) - abs(b))

# chknnum(-10, -20)
# chknnum(-10, 20)
# chknnum(10, -20)

# a = []
# for i in range(5):
#     b = int(input(f'{i+1}/5 번째 입력: '))
#     a.append(b)

# print(max(a))

# def count():
#     radi = int(input('원의 반지름을 입력하세요! 원의 넓이와 둘레를 구해줍니다! '))
#     area = radi * radi * 3.14
#     cir = (radi + radi) * 3.14
#     print(f'원의 넓이 : {area}')
#     print(f'원의 둘레 : {cir}')

# print(count())

# a = []
# for i in range(3):
#     b = int(input(f'{i+1}/3 번째 입력: '))
#     if i+1 == 1:
#         str(b * 2)
#         a.append(b)
#     elif i+1 == 2:
#         str(b * 3)
#         a.append(b)
#     else:
#         i+1 == 2:
#         str(b * 3)
#         a.append(b)


# print(a)

# def func():
#     tot = 0
#     for i in range(3):
#         tmp = int(input(f'{i+1}/3 번째 입력: '))
#         tot += (tmp * (2+i)) % 10
#     return tot

# print(func())

# class Classiccar:
#     color = '빨간색'

#     def test(self):
#         color = '파란색'
#         print('color = ', color)
#         print('self.color = ', self.color)

# father = Classiccar()
# father.test()
# father.color = '검은색'
# father.test()

# class ClassicCar:
#     def __init__(self, color): # 생성자 메소드
#         # 클래스 변수 color에 매개변수 color 할당
#         self.color = color

#     def test(self):
#         print(self.color)


# father = ClassicCar('빨간색')
# father.test()
# father.color = '검은색'
# father.test()

# class Knight:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100
#         self.mp = 20
#         self.attack_type = '근접'
#         self.attack = 30
#         self.armor = 10
#         self.potion_cnt = 3
#         print('기사 캐릭터 생성 완료!')

#     def under_attack(self, attacker):
#         # 공격타입이 마법일 경우엔 20% 데미지 가중
#         if attacker.attack_type =='마법':
#             multiple = 1.2
#         else:
#             multiple = 1
#         # 공격력 * 가중치 - 방어력
#         damage = attacker.attack * multiple - self.armor
#         self.hp -= damage
#         print(f'{self.name}: {attacker.name}님의 공격({damage})에 의해 HP[{self.hp}]')
#         # 체력이 0이 된 경우, 사망 메시지 출력
#         if self.hp <= 0:
#             print(f'{self.name}님이 {attacker.name}님에 의해 사망하였습니다.')

#     def attack_to(self, target):
#         # 공격 대상의 체력이 0 이상일 때만 실행
#         if target.hp > 0:
#             print(f'{self.name}님이 {target.name}님을 공격합니다.')
#             # 공격 대상의 피격 메소드 호출
#             target.under_attack(self)
    
#     def triple_attack(self, target):
#         # mp가 20 이상일 때만 사용 가능
#         if self.mp >= 20:
#             self.mp -= 20
#             print(f'{self.name}님이 {target.name}님을 3회 공격합니다.')
#             # 공격 대상의 under_attack메소드 3회 호출
#             for i in range(3):
#                 target.under_attack(self)

#     def use_potion(self):
#         if self.potion_cnt > 0:
#             self.hp += 20
#             if self.hp > 100:
#                 self.hp = 100
#             print(f'{self.name}님 포션 1개 사용합니다.\n남은 포션 {self.potion_cnt - 1}개 HP[{self.hp}]')
#             self.potion_cnt -= 1
#         else:
#             print('포션이 남아있지 않습니다.')

# k1 = Knight('길동')
# k2 = Knight('철수')
# print()

# k1.attack_to(k2)
# print()
# k1.attack_to(k2)
# print()
# k2.attack_to(k1)
# print()
# k2.attack_to(k1)
# print()
# k1.use_potion()
# print()
# k1.use_potion()
# print()
# k1.use_potion()
# print()
# k1.use_potion()
# print()
# k1.triple_attack(k2)
# print()

# arr = [1,2,3,4,5]
# result = []

# for i in arr:
#     if i not in result:
#         result.append(i)

# print(result)

# a = [1,2,3,4,5,6,]
# b = [1,2,3,7,8,9,]
# z = set(a) & set(b)
# print(len(z))

students = {'유재석' : 95, '정형돈' : 86, '박명수' : 56, '노홍철' : 73}
for i in range(4):
    if students[i] >= 90:
        print('A')
    else:
        print('F')