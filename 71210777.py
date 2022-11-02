class CircularQueue():

    def __init__(self, cap):
        self.capacity = cap
        self.data = [None] * cap
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.capacity == self.head):
            print("Antrian Penuh!\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.data[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.data[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("Kosong!\n")

        elif (self.head == self.tail):
            temp = self.data[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.data[self.head]
            self.head = (self.head + 1) % self.capacity
            return temp

    def display(self):
        if (self.head == -1):
            print("Kosong!")

        elif (self.tail >= self.head):
            print("Yang ada pada antrian adalah: ", end="")
            for x in range(self.head, self.tail + 1):
                print(self.data[x], end=" ")
            print()
        else:
            print("Yang ada pada antrian Circular adalah: ", end="")
            for x in range(self.head, self.capacity):
                print(self.data[x], end=" ")
            for x in range(0, self.tail + 1):
                print(self.data[x], end=" ")


circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print("Data yang dihapus adalah =", circularQueue.dequeue())
print("Data yang dihapus adalah =", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()