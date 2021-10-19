stack = [None]*10
max = 10
top = -1
base = 0

def push(item):
    global top, max

    if top < max - 1:
        top += 1
        stack[top] = item
        

    else:
        print('Stack is full')
       

def pop():
    global top, base

    if top == base - 1:
        print('Stack is empty')

    else:
        stack[top] = None
        top -= 1


print(stack)
