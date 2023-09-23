car1="honda"
car2="bmw"
car=["honda","bmw","audi","fortuner"]
print(car[0])
car.append("rolls royle")
print(car)
car.remove("honda")
print(car)
car.pop(3)
print(car)
print(len(car))
for x in car:
    print(x)
car.insert(1,"honda") 
car1=car.reverse()
print(car)
car.sort()
print(car)
d={"emp":"Name", "Sal":1000}
print(d["Sal"])
x=d.get("emp")
print(x)
