def auto_report(week):
    print('각각의 데이터를 입력 해 주세요.')
    a = input('부서 :')
    b = input('이름 :')
    c = input('업무 요약 :')
    # print(f'- {week} 주차 주간보고 -')
    # print(f'부서 : {a} 부서')
    # print(f'이름 : {b}')
    # print(f'업무요약 : {c}')
    with open(f'{week}주차.txt','w', encoding='utf8') as report_file:
        report_file.write(f'- {week} 주차 주간보고 -\n부서 : {a}부서\n이름 : {b}\n업무요약 : {c}')


auto_report(5)