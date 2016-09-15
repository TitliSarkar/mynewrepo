def myFunction(myString):
    print(myString)
    myName = raw_input("What is your name?")
    myVar = raw_input("Enter a number:")
    print(myName)
    print (myVar)
    if(myName == "Kevin" and myVar != 0):
        print("Kevin is great!")
    elif(myName == "Bob"):
        print("Bob is ok.")
    else:
        print("Hello Folks!")

myFunction("Hello 123 World")

def add(num1,num2):
    return num1+num2

myValue = add(1,4)
print(myValue)
print(add(1,4))

    
