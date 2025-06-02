f = open("file.txt", "w")

f.write("hello")
f.write("\n")
f.write("world")

f.close()

f = open("file.txt", "a")

f.write("\n")
f.write("append")
f.close()

f = open("hangul.txt", "w", encoding="utf8")

f.write("한글")
f.write("\n")
f.write("english")

f.close()

f = open("coding.txt", "w", encoding="utf8")

f.write("프로그래밍")

f.close()
