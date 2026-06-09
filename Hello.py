print('Hello Sanaullah')

def call_addition():
    print("Addition Called")

def call_subtraction():
    print("Subtraction Called")

def call_multiplication():
    print("Multiplication Called")

def call_division():
    print("Division Called")
    

while True:
    print("Enter choice")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("0 for exit")

    choice=int(input())

    if choice==1:
        call_addition()
    if choice==2:
        call_subtraction()
    if choice==3:
        call_multiplication()
    if choice==4:
        call_division()