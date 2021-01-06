'''n = int ( input (" enter your num here : ")) 
if (n % 2  != 0):
    print("weird")
elif((n%2)==0) and ( 2 < n < 5):
    print("Not weired ")
elif ((n%2)==0) and ( 6 < n <20 ):
    print("weird")
elif ((n%2)==0) and ( n > 20):
    print("Not weired")'''
    
 # new 
n=int(input("type int:"))
for i in range (0,n):
    if ( n > 0):
        print( i**2)
 
 #using WHILE loop
n=int(input("type int:"))
while( n > 0):
    for i in range (0,n):
        print( i**2)
    if (i ==5):
        break
 
        
    