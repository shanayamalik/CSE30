#===== Import section begins
from typing import Any, Dict, List, Optional, Tuple, Union
# In this problem, ONLY given external libraries are allowed
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends

#===== Problem B function begins
# follow the instruction below
# DO NOT change the function signature!
def find_paths(connection: List[List[int]], source: int, destination: int) -> List[List[int]]:
  """
  - Parameter:
    - connection: List[List[int]]
    - source: int
    - destination: int
  
  - Return: 
    - List[List[int]]
  """
  #===== Your implementation begins here
  #The adjacency list takes each vertex and associates it with a list of nearby cities, in order to represent the graph. 
  graph = {}
  for u, v in connection:
      if u not in graph:
          graph[u] = []
      graph[u].append(v)
    
  #https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
  #The dfs function is defined, taking the node and path as a parameter. 
  def dfs(node, path):
      path.append(node)
        
      #If the destination is reached, the node which was added to the path, is added to the result along with the path.
      if node == destination:
          result.append(path[:])
      else:
          if node in graph:
              for neighbor in graph[node]:
                  dfs(neighbor, path)
        
      #The current node in the path will be removed
      path.pop()
    
  #The variables for the result and path 
  result = []
  path = []
    
  dfs(source, path)
    
  return result
  #===== Your implementation ends here
  pass

#===== Problem B function ends

#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main():
  # you may add your own testing code within this function while you're
  # working on your assignment;
  # however, please remember to remove them, and re-run this testing script
  # right before you submit your work, in order to ensure your code is
  # free from syntax error

  connection = [[0,1],[0,4],[1,2],[2,3],[3,4]]
  expected_output = []
  source, destination = 2, 1
  output = find_paths(connection, source, destination)
  expected_set = set(tuple(path) for path in expected_output)
  output_set = set(tuple(path) for path in output)
  
  print("expected_output: ", expected_output)
  print("Your result    : ", output)
  if output == expected_output:
    print("test1 passed")
  else:
    print("test1 failed")
  print()

  connection = [[0,1],[1,2],[1,3],[1,5],[2,3],[2,4],[3,4],[4,5],[0,5]]
  expected_output = [[1,2,3,4,5], [1,2,4,5], [1,3,4,5], [1,5]]
  source, destination = 1, 5
  output = find_paths(connection, source, destination)
  expected_set = set(tuple(path) for path in expected_output)
  output_set = set(tuple(path) for path in output)
  
  print("expected_output: ", expected_output)
  print("Your result    : ", output)
  if output_set == expected_set:
    print("test2 passed")
  else:
    print("test2 failed")
  print()


if __name__ == "__main__":
  main()

#===== Testing scripts main function section ends
