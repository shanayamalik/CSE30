'''
Write a function that takes two lists as input and returns a list of common elements of the input lists. 
You may return the result in any order.
'''

def common_elements(list_1: list, list_2: list) -> list:
  d = {}
  o = []
  #Put all of the elements from list_1 into a dictionary
  for e in list_1:
    d[e] = True
  #Check dictionary for membership of elements from list_2
  for e in list_2:
    if e in d:
      o.append(e)
  return o

#print(common_elements([ 2, 5, 4, 1], [ 5, 3, 6, 2, 4, 10, 11, 15, 9]))

'''If the size of one of the input lists is way smaller than the other list, it wouldn't matter with this method that was used to solve the problem.  
Converting the lists to sets and taking the intersection, would be a different and efficient way to solve this. 
'''
