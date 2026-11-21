def Calculator():
    print("\n-------------A Calculator-------------")
    print("a and b are operands and c is operator\n")
    while True:
       try:
           a = float(input("Enter first number a: "))
           break
       except ValueError:
           print("Invalid input! Please enter a number.")
    while True:
       try:
           b = float(input("Enter second number b: "))
           break
       except ValueError:
           print("Invalid input! Please enter a number.")
    c = input("Enter the operator (+,-,*,/) c: ")
    if c == "+":
       print("\nAnswer of the Addition is: ", a+b)
    elif c == "-":
       print("\nAnswer of the Subtraction is : ", a-b)
    elif c == "*":
       print("\nAnswer of the Multiplication is : ", a*b)
    elif c == "/":
       if b != 0:
           print("\nAnswer of the Division is:", a / b)
       else:
           print("\nCannot divide by zero!")
    else:
       print("\ninvalid operator")
       
def km():     
    print("\n---------KM to Miles Converter---------")  
    while True: 
        try:
            k = float(input("Enter the Distance in Km: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    m = k*0.621371
    print("\nThe distance in miles is: ", m) 

def celsius():
    print("\n---------Celsius to Fahrenheit Converter---------") 
    while True:
       try:
           c = float(input("Enter the temperature in Celsius: "))
           break
       except ValueError:
           print("Invalid input! Please enter a number.")   
    f = (c * (9/5)) + 32
    print("\nThe temperature in Fahrenheit is: ", f)
      
      
while True:
    print("\n======================================")
    print("| 1. Calculator                      |")
    print("| 2. Kilometer to Miles Converter    |")
    print("| 3. Celsius to Fahrenheit Converter |")
    print("| 4. Exit                            |")
    print("======================================\n")
    
    choice = (input("Enter your choice: "))
    
    if choice == "1":
        Calculator()
           
    elif choice == "2":
        km()
       
    elif choice == "3":
        celsius()
     
    elif choice == "4":
        print("\nthank you...!!\n")
        break
    else:
        print("Invalid Choice...!!")   