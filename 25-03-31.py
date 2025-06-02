'''
x = int(input())
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")
'''


''' 
password = input()
if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다.")
'''


'''
x = int(input())
if x % 4 == 0:
    print("4의 배수")
elif x % 3 == 0:
    print("3의 배수")
elif x % 2 == 0:
    print("2의 배수")
'''


'''
x = int(input())
if 10 <= x < 20:
    print("10대")
elif 30<= x < 40:
    print("30대")
else:
    print("10, 30대가 아님")
'''


for i in range(8):
    for j in range(9):
        print(f"{i+2} * {j+1} = {(i+2)*(j+1)}")
    print("-----------")