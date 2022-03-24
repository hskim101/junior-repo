# 과목: 빅데이터언어 임동혁 월6수5
# 소속: 소프트웨어학부
# 학번: 2017203053
# 이름: 김형석
# 과제 #1

def menu1():
    while True:
        print("계단의 높이입력")
        height=input("(2이상 5이하의 높이 입력) : ")
        # 입력 값이 정수인지 검사 (실수나 문자가 입력됬을 때 프로그램 종료하지 않기 위함)
        if height.isdigit() == False:
            print("높이를 잘못 입력하셨습니다. 다시 입력해주세요.\n")
            continue
        else:
            height = int(height)
        if height<2 or height>5:
            continue
        print("계단의 칸 수 입력")
        stairs=input("(2이상 5이하의 칸 수 입력) : ")
        # 입력 값이 정수인지 검사 (실수나 문자가 입력됬을 때 프로그램 종료하지 않기 위함)
        if stairs.isdigit()==False:
            print("칸 수를 잘못 입력했습니다. 높이부터 다시 입력해주세요.\n")
            continue
        else:
            stairs=int(stairs)
        if stairs<2 or stairs>5:
            continue
        for s in range(1,stairs+1):
            for h in range(height):
                print("■"*height*s)
        break

def menu2():
    while True:
        print("더하기의 길이 입력")
        # length=int(input)) 으로 하면 문자나 실수가 들어왔을 때 프로그램이 종료되므로 문자열로 입력 받은 후 정수인지 검
        length=input("(2이상 10이하의 길이 입력) : ")
        # 입력 값이 정수인지 검사 (실수나 문자가 입력됬을 때 프로그램 종료하지 않기 위함)
        if length.isdigit() == False:
            print("길이를 잘못 입력하셨습니다. 다시 입력해주세요.\n")
            continue
        else:
            length = int(length)
        if length<2 or length>10:
            continue
        # main에서 미리 구해놓은 공백 갯수만큼 띄고 별 출력
        for l in range(length):
            print(" "*dp[length],end='')
            print("*"*length)
        for l in range(length):
            print("*"*length**2)
        for l in range(length):
            print(" "*dp[length],end='')
            print("*"*length)
        break

if __name__=="__main__":
    # 2번 메뉴 공백을 미리 계산 (Dynamic Programming)
    dp=[0]*11
    dp[2]=1

    for i in range(3,11):
        dp[i]=dp[i-1]+i-1

    while True:
        print("도형을 선택하세요")
        print("1. 계단\n2. 더하기\n3. 종료")
        menu = input()
        # 입력 값이 정수인지 검사 (실수나 문자가 입력됬을 때 프로그램 종료하지 않기 위함)
        if menu.isdigit() == False:
            continue
        else:
            menu = int(menu)
        if menu==3:
            break
        elif menu==1:
            menu1()
        elif menu==2:
            menu2()
        else:
            continue