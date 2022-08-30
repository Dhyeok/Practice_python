# 문제 1
# 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력

# 출력 문장 : XX 행 열차가 들어오고 있습니다.

# station = "인천공항"

# print(station + "행 열차가 들어오고 있습니다.")


# 문제 2
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 ~일로 선정 되었습니다.

# from random import *
# date = randint(4 , 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정 되었습니다.")

# for i in range(4):
#     print('Hello, world!', i)
    
# 문제 3
# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 :  남은 글자 중 처음 세자리 +글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#                   (nav)             (5)               (1)        (!)
# 예) 생성된 비밀번호 : nav51!

# def create_password():
#     print('인터넷 주소를 입력 해 주세요. 예) http://naver.com')
#     a = input('주소 입력 : ')
#     b = a.lstrip('http://')
#     b = b[:b.index('.')]
#     c = b.count('e')
#     d = len(b)
#     e = b[0:3]
#     print(f'생성된 비밀번호 : {e}{d}{c}!')

# create_password()

#  문제 4
#  당신의 학교에서는 파이써 코딩 대회를 주최합니다.
#  참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
#  댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#  추첨 프로그램을 작성하시오.

#  조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
#  조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#  조건3 : random 모듈의 shuffle 과 sample 을 활용

#  (출력 예제)
#   -- 당첨자 발표 --
#   치킨 당첨자 : 1
#   커피 당첨자 : [2, 3, 4]
#   -- 축하합니다 --
 
#  (활용 예제)
#  from random import *
#  1st = [1,2,3,4,5]
#  print(1st)
#  shuffle(1st)
#  print(1st)
#  print(sample(1st, 1))

# import random
# commenter = range(1, 21)
# commenter = list(commenter)
# def auto_draw():
#     print('댓글 이벤트 추첨을 시작합니다!')
#     random.shuffle(commenter)
#     print("---- 당첨자 발표 ----".center(20))
#     print(f'  치킨 당첨자 : {commenter[0]}님')
#     print(f'  커피 당첨자 : {commenter[1:5]}님')
#     print("---- 축하 합니다 ----".center(20))

# auto_draw()

#  문제 5
#  당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
#  50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

#  조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
#  조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

#  (출력문 예제)
#  [0] 1번째 손님 (소요시간 : 15분)
#  [ ] 2번째 손님 (소요시간 : 50분)
#  [0] 3번째 손님 (소요시간 : 5분)
#  ...
#  [ ] 50번째 손님 (소요시간 : 16분)

#  총 탑승 승객 : 2 분


# import random
# guest = list(range(1,51))
# time = []
# for i in range(len(guest)):
#     time.append(random.randint(5,50))
    
# dict = dict(zip(guest, time))

# def total_use():   
#     print('Cocoa 총 탑승 승객 수 프로그램을 실행 합니다.')
    
#     for a in dict:
#         for b in dict.values:
#             print(f'[{a}] {a}번째 손님 (소요시간 : {b}분)')


# total_use()

# cnt = 0 # 총 탑승 승객
# for i in range(1,51): # 1 ~ 50 이라는 수 (승객)
#     time = random.randrange(5, 51)  # 5분 ~ 50분 소요시간
#     if 5 <= time <= 15:
#         print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
#         cnt += 1
#     else:
#         print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')

# print(f'총 탑승 승객 : {cnt}분')

# def count_use():
#     cnt = 0 # 총 탑승 승객
#     for i in range(1,51): # 1 ~ 50 이라는 수 (승객)
#         time = random.randrange(5, 51)  # 5분 ~ 50분 소요시간
#         if 5 <= time <= 15:
#             print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
#             cnt += 1
#         else:
#             print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')
#     print(f'총 탑승 승객 : {cnt}분')

# count_use()

#  문제6
#  표준 체중을 구하는 프로그램을 작성하시오

#  * 표준 체중 : 각 개인의 키에 적당한 체중

#  (성별에 따른 공식)
#   남자 : 키(m) x 키(m) x 22
#   여자 : 키(m) x 키(m) x 21

#   조건1 : 표준 체중은 별도의 함수 내에서 계산
#           * 함수명 :  std_weight
#           * 전달값 : 키(height), 성별(gender)
#   조건2 : 표준 체중은 소수점 둘째자리까지 표시


#   (출력 예제)
#   키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height,gender):
#     print('표준 체중을 구하겠습니다.')
#     if gender == str('남자'):
#         std = (height * 0.01) * (height * 0.01) * 22
#         print(f'키 {height}cm 남자의 표준 체중은 {std:.2f}kg 입니다.')
#     else:
#         gender == str('여자')
#         std = (height * 0.01) * (height * 0.01) * 22
#         print(f'키 {height}cm 여성의 표준 체중은 {std:.2f}kg 입니다.')

# std_weight(173,'남자')

# def std_weight():
#     print('표준 체중을 구하겠습니다.')
#     print('키와 성별을 입력해주세요. ex) 173, 남자 or 여자')
#     height = int(input('키 입력 : '))
#     gender = input('성별 입력 : ')
#     if gender == str('남자'):
#         std = (height * 0.01) * (height * 0.01) * 22
#         print(f'키 {height}cm 남자의 표준 체중은 {std:.2f}kg 입니다.')
#     elif gender == str('여자'):
#         std = (height * 0.01) * (height * 0.01) * 21
#         print(f'키 {height}cm 여성의 표준 체중은 {std:.2f}kg 입니다.')

#     else:
#         print('입력을 제대로 해 주세요.')

# std_weight()

#  문제 7
#  당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#  보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

#  - X 주차 주간보고 -
#  부서 : 
#  이름 : 
#  업무 요약 : 

#  1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

#  조건 : 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.

# def auto_report(week):
#     print('각각의 데이터를 입력 해 주세요.')
#     a = input('부서 :')
#     b = input('이름 :')
#     c = input('업무 요약 :')
#     # print(f'- {week} 주차 주간보고 -')
#     # print(f'부서 : {a} 부서')
#     # print(f'이름 : {b}')
#     # print(f'업무요약 : {c}')
#     with open(f'{week}주차.txt','w', encoding='utf8') as report_file:
#         report_file.write(f'- {week} 주차 주간보고 -\n부서 : {a}부서\n이름 : {b}\n업무요약 : {c}')


# auto_report(5)

#  문제 8
#  주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
 
#  (출력 예제)
#  총 3대의 매물이 있습니다.
#  강남 아파트 매매 10억 2010년
#  마포 오피스텔 전세 5억 2007년
#  송파 빌라 월세 500/50 2000년

#  [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year  
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# h1 = House('강남', '아파트', '매매', '10억', '2010년')
# h2 = House('마포', '오피스텔', '전세', '5억', '2007년')
# h3 = House('송파', '빌라', '월세', '500/50', '2000년')

# houses.append(h1)
# houses.append(h2)
# houses.append(h3)

# print(f'총 {len(houses)}대의 매물이 있습니다.')
# for house in houses:
#     house.show_detail()

#  문제 9
#  동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
#  대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
#  시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

#  조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#             출력 메시지 : "잘못된 값을 입력하였습니다."
#  조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#          치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#          출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

#  [코드]
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

# while(True):
#     try:
#         print(f'[남은 치킨 : {chicken}')
#         order = int(input('치킨 몇 마리 주문하시겠습니까?'))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print('재료가 부족합니다.')
#         elif order <= 0:
#             raise ValueError
#         else:
#             print(f'[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.')
#             waiting += 1
#             chicken -= order
        
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print('잘못된 값을 입력하였습니다.')
#     except SoldOutError:
#         print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
#         break

#  문제 10 
#  프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

#  조건 : 모듈 파일명은 byme.py 로 작성

#  (모듈 사용 예제)
#  import byme
#  byme.sign()

#  (출력 예제)
#  이 프로그램은 나도코딩에 의해 만들어졌습니다.
#  유튜브 : http://youtube.com
#  이메일 : nadocoding@gmail.com

# import byme
# byme.byesoon()


