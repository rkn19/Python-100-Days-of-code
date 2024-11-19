from replit import clear
from art import logo
print(logo)
num1 = int(input("What is the first number?: "))

def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the next number?: "))
calc_func = operations[operation_symbol]

answer = calc_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
