n=int(input("enter n: "))
def Diamond(n):
   
    for i in range(1,n+1):
        print((n-i)*" ", end="")
        m=2*i-1
        print( m *"*")
        
    for i in range(1,n+1):
        print(i *" " , end="")
        m= -2*i + 2*n-1
        print(m * "*")

Diamond(n)