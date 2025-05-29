class Car():
    speed = 0
    def upSpeed(self,value) :
        self.speed += value


        print("현재속도(슈퍼클래스) : %d" % self.speed)


class Sedencar(Car):
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("현재속도(서브클래스) : %d" % self.speed)


class Truck(Car):
    pass


class Sonata(Sedencar):
    pass


sedan1, truck1 = None, None
truck1 = Truck()
sedan1 = Sedencar()
sonata1 = Sonata()


print("트럭:", end = "")
truck1.upSpeed(200)

print("승용차:", end = "")
sedan1.upSpeed(200)

print("소나타:", end = "")
sonata1.upSpeed(200)
