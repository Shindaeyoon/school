'''
print("Hello World") # Hello World

# 안녕하세요! 충남 친구들
print("안녕하세요! 충남 친구들")

print("2025") # 2025
print("Happy", "New", "Year") # Happy New Year

# 3
# 5
print("3 \n5")

print("대한민국"): print("충천남도") # SyntaxError

# 파이썬
# 재밌어~
print("파이썬 \n재밌어~")
'''


'''
print("아이엠 그라운드 자기소개 하기!")

name = []

while(True):
    a = input()
    if a == "":
        break
    name.append(a)

for i in range(len(name)):
    print(f"나는 {name[i]}")
'''


'''
from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

inp = list(input(""))

for i in range(len(inp)):
    for j in range(len(alphabet_list)):
        if alphabet_list[j] == inp[i]:
            print(alphabet_list[j])
            continue
'''


import time
import string

charset = string.ascii_letters + string.digits + string.punctuation
inp = list(input(""))
result = []

for target in inp:
    for letter in charset:
        print("\r" + "".join(result) + letter, end="", flush=True)
        time.sleep(0.0175)
        if letter == target:
            result.append(letter)
            break

print()
