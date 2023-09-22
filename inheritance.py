#parent and child class
#base and derived class

class animal:   #parent class(base class)
    def eat(self):  #method
        print("animal need food")
    def sleep(self):  #method
        print("animal need rest")   
name=''        

class dog(animal): #child class
    def bark(self):
        print("dogs bark")


dog1=dog()
#calling  methods
dog1.bark()
dog1.eat()
dog1.sleep()
dog1.name='jimmy'
print(f" my dog name is {dog1.name}")

    

