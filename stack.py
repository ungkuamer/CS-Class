stack = []
max = 10

def push(item):
    base = 0 
    top = len(stack)-1

    if top == max - 1:
        print('Stack is full')

    else:
        top += 1
        stack.append(item)

def pop():
    base = 0
    top = len(stack)-1

    if top == base - 1:
        print('Stack is empty')

    else:
        stack.pop()
        top -= 1

push(7)
push(32)
pop()
pop()

for i in range(1,11):
    push(i)

push(11)

print(stack)


