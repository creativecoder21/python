#four operation, add, subtract, multiply and division
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Welcome to the program for Simple Calculation")
print("Select any option to perform operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice=input("Enter your choice :")
    if choice in ('1','2','3','4'):
        x=int(input("Enter the first number :"))
        y=int(input("Enter the second number :"))
        if choice =='1':
            print(x, "+", y, "=", add(x,y))
        if choice =='2':
            print(x, "-", y, "=", subtract(x,y))
        if choice =='3':
            print(x, "*", y, "=", multiply(x,y))
        if choice =='4':
            print(x, "/", y, "=", divide(x,y))
        break
    else: 
        print("Invalid Input")







