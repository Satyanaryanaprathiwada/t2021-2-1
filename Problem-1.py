# Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.


class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = int(input('number-1 : '))
b = int(input('number-2: '))        
obj=cal(a,b)

choice = input('Please select operator : ')
if choice == "+":
    print("Result: ",obj.add())
elif choice == "-":
    print("Result: ",obj.sub())
elif choice == "*":
    print("Result: ",obj.multiply())    
elif choice == "/":
    print("Result: ",obj.divide())
else:
    print('Invalid option')     
print()




