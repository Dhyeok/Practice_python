import random
a = [] # 확정된 당첨 로또 번호
b = [] # 내가 선택한 로또 숫자
def playlotto():
    for i in range(6):
        winnum = random.randrange(1,46)
        while winnum in a:
            winnum = random.randrange(1,46)
        a.append(winnum)
    
    c = 0
    while c < 6:
        inpnum = int(input(f'[1 ~ 45]까지의 숫자를 입력하세요.({c + 1}/6번째 숫자)'))
        if inpnum in b:
            print('같은 수를 입력하지 마세요! 다시 숫자를 입력 해 주세요')
            continue
        if inpnum == 0:
            print('나머지 숫자는 자동으로 선택 합니다.')
            for d in range(6-c):
                num = random.randrange(1,46)
                while num in b:
                    num = random.randrange(1,46)
                b.append(num)
            break
        if 0 > inpnum or inpnum > 45:
            print('[1 ~ 45]사이로 숫자를 제대로 입력하세요')
            continue
        b.append(inpnum)
        c += 1
        print('입력번호: ',b)
    z = set(a) & set(b)
    if len(z) == 6:
        print()
        print('"축하합니다!!! 1등 당첨!!!!"')
    elif len(z) == 5:
        print()
        print('"2등 당첨!!!"')
    elif len(z) == 4:
        print()
        print('"3등 당첨!"')
    elif len(z) == 3:
        print()
        print('"5천원 당첨이요"')
    else:
        print()
        print('"꽝입니다.ㅎㅎ"')
    print()
    a.sort()
    b.sort()
    print(len(z))

      

playlotto() # 로또 번호 실행기
print('내가 선택한 번호',b) # 내가 선택한 숫자
print('당첨 번호',a) # 당첨 번호