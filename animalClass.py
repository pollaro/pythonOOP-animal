class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health:",self.health
        return self

class dog(animal):
    def __init__(self,name):
        health = 150
        super(dog, self).__init__(name,health)
    def pet(self):
        self.health += 5
        return self

class dragon(animal):
    def __init__(self,name):
        health = 170
        super(dragon, self).__init__(name,health)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(dragon,self).display_health()
        print "I am a dragon"
