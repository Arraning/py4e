def guess_number() :
    import random
    select = []
    choose = [1,2,3]
    my = []
    for select_number in choose :
        number = random.randint(0,100)
        select.append(number)
    select.sort()
    min = select[0]
    mid = select[1]
    max = select[2]
    count = 1

    while True :
        if mid in my and min in my and max in my :
            print(str(count-1)+'차 시도 만에 성공!')
            break
        else :
            print(str(count)+'차 시도')
            try :
                my_number = int(input('숫자를 추측해보세요'))
            except :
                print('숫자만 입력할 수 있습니다')
                continue
           
            if my_number in select :
                if my_number == min :
                    print('맞추셨습니다! 최솟값은',min)
                    count = count + 1
                    my.append(my_number)
                if my_number == mid :
                    print('맞추셨습니다! 중간값은',mid)
                    count = count + 1
                    my.append(my_number)
                if my_number == max :
                    print('맞추셨습니다! 최댓값은',max)
                    count = count + 1
                    my.append(my_number)
            else : 
                if count == 5 or count == 10 :
                    print('추측 실패! 다른 숫자를 입력해주세요.')
                    print('힌트! 최솟값은',str(min+10)+'보다 작고,최댓값은',str(max-10)+'보다 크다')
                    count = count + 1
                elif my_number in my :
                    print('이미 추측했던 숫자입니다. 다른 숫자를 입력하세요')
                else :
                    print('추측 실패! 다른 숫자를 입력해주세요.')
                    count = count + 1
                    my.append(my_number)
guess_number()
        
        
