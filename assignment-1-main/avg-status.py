name = input( "enter your name:")
family = input("enter your family name:")
a = float(input("first lesson:"))
b = float(input("second lesson:"))
c = float(input("third lesson:"))

avg = (a + b + c) / 3
st = "status:"
print(" name:" , name , "family name:" , family)
if avg>=17:
    print(" avg:" , avg , st, "Great")
elif avg>=12 and avg<17:
    print(" avg:" , avg , st ,  "Normal")
elif avg<12:
    print(" avg:" , avg , st , "Fail")

    