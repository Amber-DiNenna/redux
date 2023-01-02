# define functions needed: add, sub, mult, div
# print options to user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
  answer = a + b
  print(f'{a} + {b} = {answer}')

def sub(a, b):
  answer = a - b
  print(f'{a} - {b} = {answer}')

def mult(a, b):
  answer = a * b
  print(f'{a} * {b} = {answer}')

def div(a, b):
  answer = a / b
  print(f'{a} / {b} = {answer}')


add(5, 10)
sub(5, 10)
mult(5, 10)
div(5, 10)
