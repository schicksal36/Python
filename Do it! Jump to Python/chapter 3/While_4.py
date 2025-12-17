coffee = 10

while True:
    # 먼저 커피 남았는지 확인
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

    money = int(input("돈을 넣으세요: "))

    if money == 300:
        coffee -= 1
        print("커피를 줍니다.")
        print(f"남은 커피는 {coffee}개입니다.")

    elif money > 300:
        coffee -= 1
        print("커피를 줍니다.")
        print(f"잔돈 {money - 300}원을 반환합니다.")
        print(f"남은 커피는 {coffee}개입니다.")

    else:
        print("돈이 부족합니다. 꺼져^^")
        continue
