class Car(object):
    def __init__(self,name,color,speed,ratings):
        self.name = name
        self.color = color
        self.speed = speed
        self.ratings = ratings
    def getSpeed(self):
        return self.speed
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color

Lamborgini = Car("Lamborgini","Red",160,5)
Ferrari = Car("Ferrari","Blue",180,6)

print(Ferrari.getSpeed())
Lamborgini.setColor("Black")
print(Lamborgini.getColor())