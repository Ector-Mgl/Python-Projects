#Using Class to create functions to cauculate the operations
cont=0
class Cauculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #Functions of the cauculator
    def Addition(self):
        return self.a + self.b

    def Subtraction(self):
        return self.a - self.b

    def Multiplication(self):
        return self.a * self.b

    def Division(self):
        return self.a // self.b

    def Exponential(self):
        return self.a ** self.b


#Loop to the user use the cauculator


while True:

    print()
    print('=-' *35)


    # Here the user will choose the type of count he wants:
    choice= (input('\033[31mType the type of count you want to do (Type "done" to stop):\033[m\n1- Sum \n2- Subtraction\n3- Multiplication\n4- Division\n5- Exponential').strip().upper())
    #If user type 'done' the program is stopped!
    if choice in 'DONE':
        break
    # Here the program will try convert the variable choice to an intenger number (if the user doenst set it, the input will always act as a STRING)
    try:
        choice=int(choice)
    except:
        print('Please fill an intenger number')
        continue


    #Here is the variables where will fill the numbers what user want to execute the cauculation
    number_1= int(input('Type the first intenger number: '))
    number_2 = int(input('Type the second  intenger number: '))

    #Now, the game begins
    if choice==1:
        c1= Cauculator(number_1, number_2)
        print(f'\033[41m{c1.Addition()}\033[m')
        last_result = c1.Exponential()
    if choice==2:
        c2=Cauculator(number_1, number_2)
        print(f'\033[41m{c2.Subtraction()}\033[m')
        last_result = c2.Exponential()
    if choice==3:
        c3=Cauculator(number_1, number_2)
        print(f'\033[41m{c3.Multiplication()}\033[m')
        last_result = c3.Exponential()
    if choice==4:
        c4=Cauculator(number_1, number_2)
        print(f'\033[41m{c4.Division()}\033[m')
        last_result = c4.Exponential()

    if choice==5:
        c5=Cauculator(number_1, number_2)
        print(f'\033[41m{c5.Exponential()}\033[m')
        last_result= c5.Exponential()
