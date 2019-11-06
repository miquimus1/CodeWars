'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

'''
def sort_array(source_array):
    if len(source_array) == 0:
      return source_array
    odd = []
    for i in range(len(source_array)):
      if source_array[i] % 2 == 1:
        odd.append(source_array[i])
        source_array[i] = -999
    odd.sort()
    count = 0
    for i in range(len(source_array)):
      if source_array[i] == -999:
        source_array[i] = odd[count]
        count += 1

    return source_array
