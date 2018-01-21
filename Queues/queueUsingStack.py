class QueueUsingStack(object):
    __st1__ = list()
    __st2__ = list()

    def enqueue(self, elt):
        self.__st1__.append(elt)

    def dequeue(self):
        if self.empty():
            raise RuntimeError("Queue is empty")
        if len(self.__st2__) == 0:
            while len(self.__st1__) > 0:
                self.__st2__.append(self.__st1__.pop())
        return self.__st2__.pop()

    def size(self):
        return len(self.__st1__) + len(self.__st2__)

    def empty(self):
        return len(self.__st1__) == 0 and len(self.__st2__) == 0

if __name__ == '__main__':
    q = QueueUsingStack()
    choices = "1. Enqueue\n2. Dequeue\n3. Size\n4. Is Empty?\n5. Exit"
    while True:
        print choices
        choice = input("Enter your choice - ")

        if choice == 1:
            elt = raw_input("Enter element to be enqueued - ")
            q.enqueue(elt)
        elif choice == 2:
            try:
                elt = q.dequeue()
                print "Dequeued:", elt
            except Exception as e:
                print "Error occurred, queue is empty?", q.empty()
        elif choice == 3:
            print "Size of queue is", q.size()
        elif choice == 4:
            print "Queue is", "empty" if q.empty() else "not empty."
        elif choice == 5:
            break
        else:
            print "Invalid choice"
