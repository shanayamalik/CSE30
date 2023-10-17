'''
A 2-dimensional grid (or nested list) of 0s and 1s sorted in non-increasing order both row-wise and column-wise. 
Write a function that takes the grid as an input and returns the number of zeros in the grid. 
Assume that each list in the nested list has the same length (as in matrices).
'''

def num_of_zeros(grid: list) -> int:
  count = 0
  #Iterate over the lists
  for l in grid:
    #Iterate over the elements
    for i in l:
      if i == 0:
        count += 1
  return count
  
#print(num_of_zeros([[1,1,1,0],[1,1,1,0],[1,1,0,0],[0,0,0,0]]))
