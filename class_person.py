'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + "가 " + food + "을 먹습니다.")

    def __str__(self):
        return self.name + "는 " + str(self.age) + "살 입니다."

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print("열심히 일을 합니다")

    def get_salary(self):
        print("급료를 받습니다.")
        return  self.salary

e = Employee("영희", 19, 100)
print(e)
e.eat("밥")
e.work()
r = e.get_salary()
print("급료는 " + str(r) + "만원 입니다")'''


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Person 설명, 이름은 "+ self.name + " 키는 " + str(self.height)

    def __len__(self):
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None

p = Person("대윤", 18, 185)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])