class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_postfix(infix):
    stack = Stack()
    postfix = ""
    operators = set(['+', '-', '*', '/'])
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()  # Discard '('
        elif char in operators:
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                postfix += stack.pop()
            stack.push(char)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

infix = "m*n+(p-q)+r"
postfix = infix_to_postfix(infix)
print("Postfix:", postfix)


