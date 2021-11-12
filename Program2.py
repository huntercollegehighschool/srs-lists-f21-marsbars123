'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lis):
  newlis = []
  x = 1
  for i in lis[x]:
    newlis.append(i)
    x += 2
  return (newlis)