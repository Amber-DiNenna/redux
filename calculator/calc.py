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


# add(5, 10)
# sub(5, 10)
# mult(5, 10)
# div(5, 10)

user_selection = input('''
Please select your desired function from the following menu options:\n
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Exit\n
''')

while True:
  if user_selection == 'a' or user_selection == 'A':
    print('\nAddition\n')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    add(a, b)
  elif user_selection == 'b' or user_selection == 'B':
    print('\nSubtraction\n')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    sub(a, b)
  elif user_selection == 'c' or user_selection == 'C':
    print('\nMultiplication\n')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    mult(a, b)
  elif user_selection == 'd' or user_selection == 'D':
    print('\nDivision\n')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    div(a, b)
  elif user_selection == 'e' or user_selection == 'E':
    print('\nFINE BYE.\n')
    break
  else:
    print('\nPlease enter a valid letter choice from the menu options listed above.\n')
    user_selection = input('''
      Please select your desired function from the following menu options:\n
      A. Addition
      B. Subtraction
      C. Multiplication
      D. Division
      E. Exit\n
      ''')
