
 #himani=500 shekhar=340 gargi=190
#   1st 200 unit free 
#  next 200 4 rupee per unit
#  rest of units 7 
def calculatebill(lightunit):
   
    first_200unit=0
    next400units=4
    Above400Perunit=7
    if(lightunit<=200):
        print(first_200unit)
        
    
    elif(lightunit>200 and lightunit<=400):
        bill=((lightunit-200)*next400units)  
        print(bill)
        
    
   
    else:
        bill= (200*next400units)+((lightunit-400)*Above400Perunit)
        print(bill)
        
calculatebill(560)        
        
    
    

 
