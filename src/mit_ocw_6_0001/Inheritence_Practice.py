# class definition

class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:" + self.name + ":" + str(self.age)


class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        return "animal " + str(self.age) + ":" + self.name


class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def set_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("Hello")

    def __str__(self):
        return "Person " + self.name + ":" + str(self.age)


shree = Person(26, "shreedhar")
shree.set_friends("alekhya")
shree.set_friends("bunny")
print(shree)
print(shree.friends)

