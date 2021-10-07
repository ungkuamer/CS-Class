queue = [None]*5
front = 0
rear = -1
up = 4
queueful = 4
queueLen = 0

def enqueue(item):
    global queue,front,rear,up,queueful,queueLen

    if queueLen < queueful:
        if rear < up:
            rear += 1
        else:
            rear = 0

        queueLen += 1
        queue[rear] = item

    else:
        print('Queue is full, cannot enqueue')

    

def dequeue():
    global queue,front,rear,up,queueful,queueLen

    if queueLen == 0:
        print('Queue is empty, cannot dequeue')
    else:
        queue[front] = None

        if front == up:
            front = 0
        else:
            front += 1

    queueLen -= 1

enqueue(15)
enqueue(45)
dequeue()
dequeue()
dequeue()
for i in range(1,6):
    enqueue(i)

enqueue(7)
print(queue)
