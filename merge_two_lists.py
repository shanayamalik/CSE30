# -*- coding: utf-8 -*-
"""
# Programming Assignment 4, Problem A, CSE30-02, Winter 2023

## README

* Please **carefully** follow the instructions given in this template
  code
* Only edit within the allowed sections as instructed by the
  comments; you are risking your own assignment grade if you make
  edits outside those sections or deviate from the instructions
* The testing script provided at the end only performs some basic
  tests; it DOES NOT imply anything about your assignment grade
  * You may add your own tesing code in the main function while working
    on your assignment
  * **However**, you will need to remove your own testing code, and
    re-run the original testing script right before you submit the
    code, to ensure your code is free from syntax errors
"""

#===== Import section begins
# In this assignment, external libraries are NOT allowed
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends


#===== Existing classes section begins
# These class(es) are provided as part of the assignment
# DO NOT change or add anything in this section
# keep this section as is
class ListNode:
    def __init__(self, val: int, next: 'Union[ListNode, None]'=None) -> None:
        '''
        Initialize the instance of ListNode
        - Parameters:
            - val: this value of this node
            - next: it's either the next node, or None representing the end of
                    the list
        '''
        self.val = val
        self.next = next
    def __str__(self):
        '''
        string representation of the instance of ListNode
        '''
        return '{} -> {}'.format(self.val, self.next)
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

def merge_two_lists(linked_list_1: 'Union[ListNode, None]', linked_list_2: 'Union[ListNode, None]') -> ListNode:
    '''
    Merge two linked list
    - Parameters:
        - linked_list_1: the first sorted linked list; None if it's empty
        - linked_list_2: the second sorted linked list; None if it's empty
    - Returns:
        - ListNode: A sorted linked list merged from linked_list_1 and
                    linked_list_2
    '''
    #===== Your implementation begins here

    #===== Your implementation ends here
    pass

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

    linked_list_1 = ListNode(1, ListNode(3, ListNode(5)))
    linked_list_2 = ListNode(2, ListNode(4, ListNode(6)))
    linked_list_12 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    linked_list_3 = None
    linked_list_4 = None
    linked_list_34 = None

    linked_list_5 = ListNode(5)
    linked_list_6 = ListNode(2, ListNode(4, ListNode(6)))
    linked_list_56 = ListNode(2, ListNode(4, ListNode(5, ListNode(6))))

    print('Test case 1')
    linked_list_your_res = merge_two_lists(linked_list_1, linked_list_2)
    print('First linked list:  ', linked_list_1)
    print('Second linked list: ', linked_list_2)
    print('Expected result:    ', linked_list_12)
    print('Your result:        ', linked_list_your_res)
    type_match = type(linked_list_12) == type(linked_list_your_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:        ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 2')
    linked_list_your_res = merge_two_lists(linked_list_3, linked_list_4)
    print('First linked list:  ', linked_list_3)
    print('Second linked list: ', linked_list_4)
    print('Expected result:    ', linked_list_34)
    print('Your result:        ', linked_list_your_res)
    type_match = type(linked_list_34) == type(linked_list_your_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:        ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 3')
    linked_list_your_res = merge_two_lists(linked_list_5, linked_list_6)
    print('First linked list:  ', linked_list_5)
    print('Second linked list: ', linked_list_6)
    print('Expected result:    ', linked_list_56)
    print('Your result:        ', linked_list_your_res)
    type_match = type(linked_list_56) == type(linked_list_your_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:        ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()


if __name__ == '__main__':
    main()

#===== Testing scripts main function section ends
