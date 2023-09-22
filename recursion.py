def fibonnacci(i):
        if(i==0):
            return 0
        elif(i==1):
            return 1
        return  fibonnacci(i-2)+fibonnacci(i-1)       
        
nterms=int(input("enter a number "))          
for i in range(nterms):
    print(fibonnacci(i))
    

    
  
    

    
    

    
    