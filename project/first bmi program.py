
print('안녕하세요. 당신의 BMI를 구해 드립니다.')

heiinput = int(input('키를 입력 해 주세요.')) / 100
print(heiinput)

weiinput = int(input('몸무게를 입력 해 주세요'))
print(weiinput)


bmi = weiinput / (heiinput ** 2)

print(f'당신의 BMI 수치는 {round(bmi, 2)} 입니다.')

if bmi <= 18.5:
    print('저체중 입니다.')
elif bmi >= 18.5 and bmi <= 22.9:
    print('정상 입니다. ^^')
elif bmi >= 23.0 and bmi <= 24.9:
    print('과체중 입니다.')
else:
    print('비만 입니다.')

