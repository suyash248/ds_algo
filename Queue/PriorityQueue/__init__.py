from Heap.BinaryHeap.maxHeap import MaxHeap
from copy import deepcopy


class PriorityQueue(object):
    def __init__(self, pq_capacity=10):
        self._pq_capacity_ = pq_capacity
        self._pq_size_ = 0
        self._pq_heap_ = MaxHeap(pq_capacity)

    def insert(self, item, priority):
        res = False
        if self.is_full():
            print "Priority queue is full, please delete older items in order to insert newer ones."
            return res
        e = Entry(item, priority)
        res = self._pq_heap_.insert(e)
        if res:
            self._pq_size_ += 1
        return res

    def delete_item_with_highest_priority(self):
        res = False
        if self.is_empty():
            print "Priority queue is empty"
            return res
        res = self._pq_heap_.delete_max()
        if isinstance(res, bool) and res == False:
            pass
        else:
            self._pq_size_ -= 1
        return res

    def get_item_with_highest_priority(self):
        if self.is_empty():
            print "Priority queue is empty"
            return False
        return self._pq_heap_.get_max()

    def is_full(self):
        return self._pq_size_ >= self._pq_capacity_

    def is_empty(self):
        return self._pq_size_ <= 0

    def pq_print(self):
        return deepcopy(self._pq_heap_.heap_arr()[0:self.pq_size()])

    def pq_size(self):
        return self._pq_size_

    def pq_capacity(self):
        return self._pq_capacity_


class Entry(object):
    """
    Represents an entry(combination of item & priority) of priority queue.
    """
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __str__(self):
        return "({}:{})".format(self.item, self.priority)

    def __repr__(self):
        return "({}:{})".format(self.item, self.priority)

    def __le__(self, other):
        return self.priority <= other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __ne__(self, other):
        return self.priority != other.priority


def test():
    pq_arr_test = ["5 2", "6 1", "2 7", "4 3", "7 0", "8 5", "9 6"]
    pq_capacity = len(pq_arr_test)

    pq = PriorityQueue(pq_capacity)

    mh_test = MaxHeap(pq_capacity)

    for item_priority in pq_arr_test:
        item_priority = item_priority.split(" ")
        item = int(item_priority[0].strip())
        priority = int(item_priority[1].strip())
        mh_test.insert(priority)
        pq.insert(item, priority)

    print pq.pq_arr()
    print mh_test.heap_arr()
    print "Element with highest priority: ", pq.get_item_with_highest_priority()


if __name__ == '__main__':
    pq_capacity = input("Please enter the size/capacity of priority queue - ")
    pq = PriorityQueue(pq_capacity)

    menu = """
    Menu:
        1. Insert.
        2. Print priority queue.
        3. Get item with maximum priority.
        4. Delete item with maximum priority.
        5. Get the size and capacity of priority queue.
        6. Stop.
    """
    print menu
    while True:
        try:
            choice = input("Please enter your choice - ")
        except:
            print "Incorrect choice, please select from menu."
            continue
        try:
            if choice == 1:
                item_priority = raw_input("Enter item & priority separated by a white-space - ")
                item_priority = item_priority.split(" ")
                item = item_priority[0].strip()
                priority = item_priority[1].strip()
                res = pq.insert(item, priority)
                print res
                continue
            if choice == 2:
                print pq.pq_print()
                continue
            if choice == 3:
                res = pq.get_item_with_highest_priority()
                print res
                continue
            if choice == 4:
                res = pq.delete_item_with_highest_priority()
                print res
                continue
            if choice == 5:
                print "Size : {} | Capacity: {}".format(pq.pq_size(), pq.pq_capacity())
                continue
            if choice == 6:
                break
        except Exception as ex:
            print "Error occurred while performing last operation(choice: {}):".format(choice)
            print ex.message, ex.args

        print menu
