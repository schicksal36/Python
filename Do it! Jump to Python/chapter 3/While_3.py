coffee = 10
money = 300 

while money :
    print("돈을 넣었습니다.")
    coffee -=1
    print("남은 커피는 %d를 " %coffee)
    if coffee == 0:
        print("커피가 다떨어졌습니다.")
        break