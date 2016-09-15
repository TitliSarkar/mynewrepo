#Returns the sum of num1 and num1
def add(num1,num2):
    return num1 + num2

#Returns the difference of num1 and num1
def sub(num1,num2):
    return num1 - num2

#Returns the multiplication of num1 and num1
def mul(num1,num2):
    return num1 * num2

#Returns the division of num1 and num1
def div(num1,num2):
    return num1 / num2

def main():
    operation = raw_input("What do you want to do(+,-,*,/) : ")
    if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
            #invalid operation
            print("You must enter a valid operation")
    else:
            var1 = int(raw_input("Enter number1: "))
            var2 = int(raw_input("Enter number2: "))
            if(operation == '+'):
                print(add(var1,var2))
            elif(operation == '-'):
                print(sub(var1,var2))
            elif(operation == '*'):
                print(mul(var1,var2))
            elif(operation == '/'):
                print(div(var1,var2))
                                 
main()
          
        
        
        
        
        
        
        
        
        
