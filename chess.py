n= int(input("please enter row: "))
m= int(input("please enter column: "))

def chess(n: int,m: int):
 list1=[]
 
 j=1
 for i in range(1,n+1): 
    while j < m+1:
      if j % 2 !=0:
         list1.append("*")
         j+=1
      elif j%2==0:
        list1.append("#")
        j+=1
    print(*list1)            
 


chess(n, m)