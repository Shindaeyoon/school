'''class Car:
    def __init__(self, type, speed):
        self.tyoe = type
        self.speed = speed

    def move(self):
        print(self.tyoe + "가" + str(self.speed) + "속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount

c = Car("스포츠카", 100)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()'''


'''class Car:
    count = 0

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
print(Car.get_count())'''


