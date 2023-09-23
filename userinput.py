# a = (input("Enter a number"))
# b = (input("Enter 2nd number"))
# print("The sum of two number is: ", a+b)

# a = input("Enter your first Name:")
# b = input("Enter your surname:")
# print("your full name is:", a +" "+ b)

# num = int(input("Enter a number:"))
# if(num == 0):
#     print("the num is zero")
# elif(num > 0):
#     print("positive")
# else:
#     print("negative")

# year = int(input("Enter any year:"))
# if(year % 4 == 0 or year % 100 == 0)and(year % 400 == 0):
#     print("Leap Year")
# else:
#     print("not a leap year")

# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter 2nd number:"))
# num3 = int(input("Enter 3rd number:"))
# if(num1 > num2 and num1 > num3):
#     print(num1,"is greater.")
# elif(num2 > num1 and num2 > num3):
#     print(num2, "is greater.")
# else:
#     print(num3, "is greater.")

num=int(input ("ENTER A NUMBER"))
original=num
reverse=0
while num>0:
    
    remainder=num%10
    reverse=remainder+10*reverse
    num=num//10  
 
print(reverse)
if(original==reverse):{
    print("palidrome")
}
else:
    print("not a palidrome")
   


    