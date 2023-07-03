a = int(input("enter A:"))
b = int(input("enter B:"))
c = int(input("enter C:"))

if a + b > c and a + c > b and b + c > a :
    print("yes, we made thar triangle :)")
else:
    print("No, we could not make that triangle! :(")
    
