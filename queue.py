queue = [None]*5
front = 0
rear = -1
up = 5
queueful = 5
queueLen = 0

def enqueue(item):
    global queue,front,rear,up,queueful,queueLen

    if queueLen < queueful:
        if rear < up:
            rear += 1
        else:
            rear = 0

    else:
        print('Queue is full, cannot enqueue')

    queueLen += 1
    queue[rear] = item

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

    queueLen +- 1

enqueue(15)
enqueue(45)
dequeue()
dequeue()
enqueue(4)
print(queue)
