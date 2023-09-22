# x=lambda a:a+10
# print(x(6))
# x = lambda a,b: a * b
# print(x(5,6))
# y = lambda a,b,c : a+b+c
# print(y(6,2))
def myfunc(n):
  return lambda a : a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(7))
print(mytripler(7))
