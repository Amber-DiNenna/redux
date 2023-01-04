def binary_search(list, element):
  middle = 0
  start = 0
  end = len(list)
  steps = 0

  while (start <= end):
    print(f'''
    Steps: {steps}
    {list[start:end+1]}
    ''')

    steps = steps + 1
    middle = (start + end) // 2

    if element == list[middle]:
      return middle
    if element < list[middle]:
      end = middle - 1
    else:
      start = middle + 1

  return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12

binary_search(my_list, target)





# splits list data in two by index position
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# works by adding first index position [0] and last index position [9] and dividing the result by 2 (= 4.5)
# (0+9)/2 = 4.5
# rounds off?
# compares to target value
# if target value = 3, it compares it to ___ in the list and discards the other half of the list values until it reaches the target?


# a function that takes a list and target parameter
# multible variables: middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is made
# conditions to track target position
