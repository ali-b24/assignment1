import math
import mpmath

a = float(input("please enter first number:"))

op = input("what operation would you like?")
if op == "sin" or op =="cos" or op == "tan" or op == "cot" or op == "fact" or op == "sqr":
    
    if op == "sqr":
        result = math.sqrt(a)
    if op == "sin":
        result = math.sin(math.degrees(a))
    if op == "cos":
        result = math.cos(math.degrees(a))
    if op == "tan":
        result = math.tan(math.degrees(a))    
    if op == "cot":
        result = mpmath.cot(math.degrees(a)) 
    if op == "fact":
        result = math.factorial(int(a))
     

else:
    b = float(input("please enter second number:"))  
    if op == "+":
        result = a + b
    if op == "-":
        result = a - b
    if op == "*":
        result = a * b
    if op == "/":
        if b == 0:
            result = "not a number!"
        else:    
            result = a / b   
        
print(result)