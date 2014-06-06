class Person:
    """This is an example showing OOP principles in Python"""
    def __init__(self, name):
        self.name = name
        print "create person %s" % self.name
    
    def sayhello(self):
        print "hello, my name is", self.name

    def __del__(self):
        print "%s says bye" % self.name
 
class Woman(Person):
    def wear(self):
        print "I wear skirt"
    def __womanmethod(self):
        print "Woman power"
        
class Man(Person):
    def wear(self):
        print "I wear shirt"

A = Woman("Alice")
B = Man("Bob")
A.sayhello()
A._Woman__womanmethod()
B.sayhello()
A.wear()
B.wear()

print "Person.__doc__:", Person.__doc__
print "Person.__name__:", Person.__name__
print "Person.__module__:", Person.__module__
print "Person.__bases__:", Person.__bases__
print "Woman.__bases__:", Woman.__bases__
print "Man.__bases__:", Man.__bases__
print "Person.__dict__:", Person.__dict__