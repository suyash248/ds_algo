# https://www.youtube.com/watch?v=ufwPuyxkNVE&list=PLeIMaH7i8JDjd21ZF6jlRKtChLttls7BG
"""
Get Minimum Element from Stack in Constant O(1) time complexity
"""

class MinStack(object):
    __primary_stack__ = list()
    __secondary_stack__ = list()

    # Time complexity: O(1)
    def push(self, elt):
        self.__primary_stack__.append(elt)
        if len(self.__secondary_stack__) == 0 or elt < self.__secondary_stack__[-1]:    # elt < secondary_stack[top]
            self.__secondary_stack__.append(elt)

    # Time complexity: O(1)
    def pop(self):
        if len(self.__primary_stack__) == 0:
            raise IndexError("Stack is empty")
        popped_elt = self.__primary_stack__.pop()
        if popped_elt == self.__secondary_stack__[-1]:      # elt == secondary_stack[top]
            self.__secondary_stack__.pop()
        return popped_elt

    # Time complexity: O(1)
    def min(self):
        return self.__secondary_stack__[-1]

    def __str__(self):
        return str(self.__primary_stack__) + "\n" + str(self.__secondary_stack__)


if __name__ == '__main__':
    stack = MinStack()
    choices = {
        1: "Push",
        2: "Pop",
        3: "Find minimum",
        4: "Print",
        5: "Exit"
    }
    choices = '\n'.join(['{}. {}'.format(k, v) for k, v in choices.items()])

    while True:
        print "\n" + choices + "\n"
        try:
            choice = input("Enter your choice - ") or 0
        except:
            choice = 0

        if choice == 1:
            elt = raw_input("Please enter element to be pushed - ")
            stack.push(elt)
        elif choice == 2:
            try:
                popped_elt = stack.pop()
                print "Popped - ", popped_elt
            except IndexError as ie:
                print "Error occurred", ie
        elif choice == 3:
            min_elt = stack.min()
            print "Minimum element -", min_elt
        elif choice == 4:
            print "Primary and secondary stacks -"
            print stack
        elif choice == 5:
            print "Thank you!"
            break
        else:
            print "Invalid choice"
            continue
