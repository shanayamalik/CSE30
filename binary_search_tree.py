#===== Import section begins
# In this assignment, No external libraries are allowed 
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends


#===== Existing classes section begins
# These class(es) are provided as part of the assignment
# DO NOT change or add anything in this section
# keep this section as is
class BinarySearchTree:
    def __init__(self, val: int, left: 'Union[BinarySearchTree, None]'=None, right: 'Union[BinarySearchTree, None]'=None) -> None:
        '''
            Constructor for a node of a BST
            - Parameters:
                - val: the value stored in the respective node
                - left: the left branch of the tree. defaults to None if no branch is given
                - right: the right branch of the tree. defaults to None if no branch is given
            - Returns:
                - None
        '''
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        """
        Str getter function which prints the BST in a String form for visual aid
            - Parameters:
            -None
            - Returns:
            - str representation of BST
        """
        return '{} [{}] [{}]'.format(self.val, self.left, self.right)
pass
#===== Existing classes section ends


#===== Helper classes/functions section begins
# You may add your own classes or functions within this section
# **class** and **function** only!
# any statement that is not encapsulated inside a class or function
# may result in 0 grade

#===== Helper classes/functions section ends


#===== Problem A function begins
# follow the instruction below
# DO NOT change the function signature!
def get_closest_numbers(tree: BinarySearchTree, f: float, p: int) -> 'List[int]': #please use a function with this naming convention for consistent function calls when grading
    '''
    return the p-closest values to f
    - Parameters:
        - tree: a given BST in the form of a BinarySearchTree class object
        - root: the root node of the BST
        - f: the float which is the target value
        - p: the amount of closest values to f to return
    - Returns:
        - List: list of p values within the BST which are closest to f
    '''
    #===== Your implementation begins here
    p_closest=[] #variables do not have to keep this naming convention, but should return a list with the corresponding output

    return p_closest
    #===== Your implementation ends here
#===== Problem A function ends

#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main() -> None: 
    # you may add your own testing code within this function while you're 
    # working on your assignment;
    # however, please remember to remove them, and re-run this testing script
    # right before you submit your work, in order to ensure your code is
    # free from syntax error

    #Below is code for constructing BST trees based on the examples provided in canvas
    #Example 1 tree
    myTree1=BinarySearchTree(val=5)
    myTree1.right=BinarySearchTree(val=6)
    myTree1.left=BinarySearchTree(val=3)
    myTree1.left.right=BinarySearchTree(val=4)
    myTree1.left.left=BinarySearchTree(val=2)

    #Example 2 tree
    myTree2=BinarySearchTree(val=3)

    #Example 3 tree
    myTree3=BinarySearchTree(val=8)
    myTree3.left=BinarySearchTree(val=3)
    myTree3.left.left=BinarySearchTree(val=1)
    myTree3.left.right=BinarySearchTree(val=6)
    myTree3.left.right.left=BinarySearchTree(val=4)
    myTree3.left.right.right=BinarySearchTree(val=7)
    myTree3.right=BinarySearchTree(val=10)
    myTree3.right.right=BinarySearchTree(val=14)
    myTree3.right.right.left=BinarySearchTree(val=13)


    f_1 = 4.82
    p_1 = 2
    output1=get_closest_numbers(myTree1, f_1, p_1)
    expectedOutput1 = [4, 5]
    print('Input Tree:         ', myTree1)
    print('Input F:            ', f_1)
    print('Input P:            ', p_1)
    print('Expected result:    ', expectedOutput1)
    print('Your result:        ', output1)
    if output1 is not None and sorted(output1)==expectedOutput1:
        print("Test 1 passed")
    else:
        print("Test 1 incorrect output")
    print()
    
    f_2 = 1.2
    p_2 = 1
    output2=get_closest_numbers(myTree2, f_2, p_2)
    expectedOutput2 = [3]
    print('Input Tree:         ', myTree2)
    print('Input F:            ', f_2)
    print('Input P:            ', p_2)
    print('Expected result:    ', expectedOutput2)
    print('Your result:        ', output2)
    if output2 is not None and sorted(output2)==expectedOutput2:
        print("Test 2 passed")
    else:
        print("Test 2 incorrect output")
    print()

    f_3 = 99.0
    p_3 = 4
    output3=get_closest_numbers(myTree3, f_3, p_3)
    expectedOutput3 = [8, 10, 13, 14]
    print('Input Tree:         ', myTree3)
    print('Input F:            ', f_3)
    print('Input P:            ', p_3)
    print('Expected result:    ', expectedOutput3)
    print('Your result:        ', output3)
    if output3 is not None and sorted(output3)==expectedOutput3:
        print("Test 3 passed")
    else:
        print("Test 3 incorrect output") 
    print() 

if __name__ == '__main__':
    main()
#===== Testing scripts main function section ends
