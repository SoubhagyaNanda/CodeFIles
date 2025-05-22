# Create a Calculator Class
# Implement a class with methods: add(), subtract(), multiply(), divide().

'''
class Calculator:
    def add(self, numbers):
        return sum(numbers)

    def sub(self, numbers):
        result= numbers[0]
        for num in numbers[1:]:
            result -= num
            return result

    def multiply(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
            return result

    def divide(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Error: Division by zero!"
            result /= num
        return result


cal = Calculator()

while True:
    print("1. add")
    print("2. sub")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")

    choice = input("Enter Your Choice From (1-5): ")

    if choice == '5':
        print('Exiting calculator')
        break

    try:
        num = input('Enter your number separate by spaces: ')
        numbers = list(map(float, num.strip().split()))
        if len(numbers)> 2:
            print('Enter atleast two numbers: ')
            continue

    except ValueError as VE:
        print("Envalid input..")
        continue

    if choice=='1':
        print('result', cal.add(numbers))
    elif choice=='2':
        print('result', cal.sub(numbers))
    elif choice=='3':
        print('result', cal.multiply(numbers))
    elif choice=='4':
        print('result', cal.divide(numbers))
    else:
        print("Invalid choice")
'''


#Student Class
#Create a Student class that stores name, age, and marks. Add a method is_pass() that returns True if marks > 40.

'''
class Students:
    def details(self,name, age, marks):
        self.name= name
        self.age = age
        self.marks= marks

    def is_pass(self):
        if self.marks>40:
            print(f'{self.name} is pass with {self.marks}')
        else:
            print(f'{self.name} candidate is fail !!')

school= Students()
school.details('soubhagyananda', 24, 22)
school.is_pass()
'''


# Function to Check Prime
# Define a function is_prime(n) to return True if the number is prime.

'''
def is_prime(n, count):
    if n>=1:
        for i in range(1, n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        return False
    else:
        print('Value is too small')

num= int(input('Enter your number: '))
is_prime(num, 0)
'''


# Function to Return Factorial of a Number Using Recursion
# Input: 5 → Output:

'''
def factorial(num):
        if num == 0:
            return 1
        return num*factorial(num-1)
data= int(input('Enter your number: '))
print(factorial(data))
'''


# Bank Account Class
# Create a BankAccount class with methods: deposit(), withdraw(), and get_balance().

class BankAccount:
    def deposit(self):
        pass