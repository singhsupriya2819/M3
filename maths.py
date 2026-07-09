def add(p,q):
    print("The sum is", p+q)

def sub(p,q):
    print("The substraction is", p-q)

def multiply(p,q):
    print("The multiplication is", p*q)

def division(p,q):
    print("The division is", p/q)

      
# Now we will take inputs from the user    
print ("Please select the operation.")    
print ("a. add")    
print ("b. sub")    
print ("c. multiply")    
print ("d. divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
p = int (input ("Please enter the first number: "))    
q = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (p, " + ", q, " = ", add(p, q))    
    
elif choice == 'b':    
   print (p, " - ", q, " = ", sub(p, q))    
    
elif choice == 'c':    
   print (p, " * ", q, " = ", multiply(p, q))  

elif choice == 'd':    
   print (p, " / ", q, " = ", divide(p, q))    
else:    
   print ("This is an invalid input")    