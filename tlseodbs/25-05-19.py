'''import  sys

while True:
    print("종료하려면 exit를 입력하세요.")
    user_input = input("> ")
    if user_input == "exit":
        sys.exit()'''


import repeater

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

repeater.repeat(s, int(n))
repeater.repeat(s)
repeater.once(s)

'''from sys import exit

while True:
    print("종료하려면 exit를 입력하세요.")
    user_input = input("> ")
    if user_input == "exit":
        exit()'''

'''from repeater import repeat, once

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

repeat(s, int(n))
repeat(s)
once(s)'''


'''from sys import *

while True:
    print("종료하려면 exir를 입력하세요.")
    user_input = input("> ")
    if user_input == "exit":
        exit()'''


'''from repeater import  *

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

repeat(s, int(n))
repeat(s)
once(s)'''

'''import sys as s
sys = ("반복 시스템입니다.")

while True:
    print(sys)
    print("종료하려면 exit를 입력하세요")
    user_input = input("> ")
    if user_input == "exit":
        s.exit()'''

'''import  repeater as r

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

r.repeat(s, int(n))
r.repeat(s)
r.once(s)'''


'''import sys
print(sys.path)'''