class Person:
    def __init__ (self,name,lastname):
        self.name = name
        self.lastname = lastname

    def full_name(self):
        return (self.name + self.lastname)
    
person1 = Person("test","testauskas")

print(person1.full_name())