from art import logo
print(logo)

def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2
  
number1 = float(input("What's the First Number"))
number2 = float(input("What's the Second Number"))

operations={
  "+" : add(number1,number2),
  "-" : substract(number1,number2),
  "*" : multiply(number1,number2),
  "/" : divide(number1,number2)
}

for key in operations:
  print(key)

operation_symbol = input("Choose an operation from the line above")

result = operations[operation_symbol]

print(f"{number1} {operation_symbol} {number2} = {result}")