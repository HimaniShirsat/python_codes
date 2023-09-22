#if u r below than 5 = free
#6-14 = 150
#14-18 = 250
#above 18 = 300

age = int(input("Enter your age: "))
if(age <= 5):
    print("Free")
elif(age >= 6 and age < 14):
    print("Ticket price 150")
elif(age >= 14 and age < 18):
    print("Ticket price 250")
else:
    print("Ticket price 300")