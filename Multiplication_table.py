
n= int(input("please enter first number: "))
m= int(input("please enter secound number: "))

def multi_table(n,m):
   
   for i in range(1,n+1):
      print()
      for j in range(1,m+1): 
         print(i*j , end="")

        
    
    
multi_table(n,m)