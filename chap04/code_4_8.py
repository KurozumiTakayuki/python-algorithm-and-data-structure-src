class MyStack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def __str__(self):
        return str(self.data)


def check_parentheses(text):
    stack = MyStack()
    for c in text:
        if c == '(':
            stack.push(c)

        if c == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    if len(stack.data) == 0:
        return True
    else:
        return False


def main():
    my_text = '(1, 5, 7, (3, 4, 8),(2, 9, 8)'
    result = check_parentheses(my_text)
    if result:
        print("OK")
    else:
        print("NG")


main()
