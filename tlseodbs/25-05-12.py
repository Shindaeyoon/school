'''
width = 3
height = 5
print("가로 ", width, " 세로 ", height, "인 삼각형의 넓이 : ", 3* 5 * 1/2)
print("가로 ", width, " 세로 ", height, "인 사각형의 넓이 : ", 3* 5)
'''

'''
import  area2

area2.print_area(10, 20)
area2.print_area(20,30)

for i in range(11,15):
    area2.print_area(i,20)

print("가로 30 세로 10인 사각형의 넓이는 : ", area2.box_area(30,10))
print(area2.__name__)
'''


import sys
def tri_area(width, height):
    return width * height * 1/2

def box_area(width, height):
    return width * height

def print_area(width, height):
    print("가로 ", width, " 세로 ", height, "인 삼각형의 넓이 : ", tri_area(width, height))
    print("가로 ", width, " 세로 ", height, "인 사각형의 넓이 : ", box_area(width, height))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print_area(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("사용법 : pythn area3 가로 세로")
''''''

'''
import sys

def repeat_str(mag, n):
    return mag * n

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(repeat_str(sys.argv[1], int(sys.argv[2])))
    else:
        print("사용법: python repeat_str 문자열 숫자")
'''
