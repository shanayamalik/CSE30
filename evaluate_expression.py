class EvalExpression:

  def evaluate(self, s: str) -> int:

    #Define two stacks, one for operands and one for operators
    operands = []
    operators = []
    
    #Define a dictionary to store the order in which each operation should work.
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    def perform_operation(operator):
        b = operands.pop()
        a = operands.pop()
        if operator == '+':
            operands.append(a + b)
        elif operator == '-':
            operands.append(a - b)
        elif operator == '*':
            operands.append(a * b)
        elif operator == '/':
            operands.append(a // b)

    #This will iterate through the expression and calculate the result
    i = 0
    while i < len(s):
        char = s[i]
        
        #If the character is a digit, the full number will be extracted and and pushed to the stack of operands
        if char.isdigit():
            num = int(char)
            j = i + 1
            while j < len(s) and s[j].isdigit():
                num = num * 10 + int(s[j])
                j += 1
            operands.append(num)
            i = j - 1
        
        #If the character is an operator, pop the top elements of the operators stack and perform the operation. 
        elif char in precedence:
            while len(operators) > 0 and precedence[operators[-1]] >= precedence[char]:
                perform_operation(operators.pop())
            operators.append(char)
      
        i += 1

    #Perform the remaining operations in the operators stack
    while len(operators) > 0:
        perform_operation(operators.pop())

    #Return the final result
    return operands[-1]

#Create an instance of the EvalExpression class and evaluate the expression
#evaluator = EvalExpression()
#result = evaluator.evaluate("3+8 / 2")
#print(result) 
