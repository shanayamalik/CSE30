#===== Import section begins
from typing import Any, Dict, List, Optional, Tuple, Union
import collections
import itertools
# In this problem, ONLY given external libraries are allowed
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends

#===== Problem C function begins
# follow the instruction below
# DO NOT change the function signature!

def find_largest_pattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
  """
  - Parameter:
    - username: List[str]
    - timestamp: List[str]
    - website: List[str]
  
  - Return: 
    - List[str]
  """
  #===== Your implementation begins here
  #Create a dictionary, with the keys being the usernames and the values are a list of visits to the website by the user
  visits_by_user = {}
  for i in range(len(username)):
      u = username[i]
      w = website[i]
      t = timestamp[i]
      if u not in visits_by_user:
          visits_by_user[u] = []
      visits_by_user[u].append((t, w))

  #The visits on the website per user are sorted according to the timestamps
  for u in visits_by_user:
        visits_by_user[u].sort()

  #There are three potential combinations for each website, and the amount of back-to-back visits is counted
  scores = {}
  for u in visits_by_user:
      visits = visits_by_user[u]
      n = len(visits)
      for i, j, k in itertools.combinations(range(n), 3):
          w1 = visits[i][1]
          w2 = visits[j][1]
          w3 = visits[k][1]
          if w1 != w2 and w2 != w3:
              if visits[i][0] < visits[j][0] < visits[k][0]:
                  pattern = (w1, w2, w3)
                  if pattern not in scores:
                      scores[pattern] = set()
                  scores[pattern].add(u)

  # Find the pattern with the highest score and smallest lexicographical order
  best_pattern = None
  best_score = 0
  for pattern, users in scores.items():
      score = len(users)
      if score > best_score or (score == best_score and pattern < best_pattern):
          best_pattern = pattern
          best_score = score

  return list(best_pattern)
  #===== Your implementation ends here
  pass

#===== Problem C function end

#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main():
  # you may add your own testing code within this function while you're
  # working on your assignment;
  # however, please remember to remove them, and re-run this testing script
  # right before you submit your work, in order to ensure your code is
  # free from syntax error
  username = ["bob","bob","bob","john","john","john","john","mike","mike","mike"]
  timestamp = [1,2,3,4,5,6,7,8,9,10]
  website = ["song","page","faq","song","cart","maps","song","song","page","faq"]
  output = find_largest_pattern(username, timestamp, website)
  expected_output = ["song","page","faq"]

  print("expected_output: ", expected_output)
  print("Your result    : ", output)
  if output == expected_output:
    print("test1 passed")
  else:
    print("test1 failed")
  print()

if __name__ == "__main__":
  main()

#===== Testing scripts main function section ends
