class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def __repr__(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        return "Stack: " + " -> ".join(map(str, values))

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []

    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # pop '('
        else:  # Operator
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence.get(token, 0) <= precedence.get(stack.peek(), 0)):
                output.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

def infix_to_prefix(expression):
    def reverse_expression(expr):
        return expr[::-1]

    reversed_expr = reverse_expression(expression)
    # Replace ( with ) and vice versa
    reversed_expr = reversed_expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    postfix_expr = infix_to_postfix(reversed_expr)
    prefix_expr = reverse_expression(postfix_expr)

    return prefix_expr

def evaluate_postfix(expression):
    stack = Stack()

    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 // operand2)
            elif token == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()

def evaluate_prefix(expression):
    stack = Stack()

    for token in reversed(expression):
        if token.isdigit():
            stack.push(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 // operand2)
            elif token == '^':
                stack.push(operand1 ** operand2)

    return stack.pop()

# Example usage
if __name__ == "__main__":
    # Input infix expression
    infix_expr = "3+(2*4)-5"
    print("Infix Expression:", infix_expr)

    # Infix to Postfix
    postfix_expr = infix_to_postfix(infix_expr)
    print("Postfix Expression:", postfix_expr)

    # Infix to Prefix
    prefix_expr = infix_to_prefix(infix_expr)
    print("Prefix Expression:", prefix_expr)

    # Evaluate Postfix
    postfix_eval = evaluate_postfix(postfix_expr)
    print("Postfix Evaluation:", postfix_eval)

    # Evaluate Prefix
    prefix_eval = evaluate_prefix(prefix_expr)
    print("Prefix Evaluation:", prefix_eval)


