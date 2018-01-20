"""
Algorithm -
1) Push the first element to stack.
2) for i=1 to len(arr):
    a) Mark the current element as `cur_elt`.
    b) If stack is not empty, then pop an element from stack and compare it with `cur_elt`.
    c) If `cur_elt` is greater than the popped element, then `cur_elt` is the next greater element for the popped element.
    d) Keep popping from the stack while the popped element is smaller than `cur_elt`. `cur_elt` becomes the
        next greater element for all such popped elements.
    g) If `cur_elt` is smaller than the popped element, then push the popped element back to stack.
3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next greater element for them.
"""

# Time Complexity: O(n)
def next_greater(arr):
    stack = list()
    stack.append(arr[0])

    for cur_elt in arr[1:]:
        if len(stack) > 0:
            popped_elt = stack.pop()
            if popped_elt < cur_elt:
                while popped_elt < cur_elt:
                    print "{} -> {}".format(popped_elt, cur_elt)
                    # Keep popping element until either stack becomes empty or popped_elt >= cur_elt
                    if len(stack) == 0: break
                    popped_elt = stack.pop()
            else:
                # If popped_elt >= cur_elt, push it back to stack and continue
                stack.append(popped_elt)
            # Push cur_elt to stack
        stack.append(cur_elt)

    while len(stack) > 0:
        print "{} -> {}".format(stack.pop(), -1)


if __name__ == '__main__':
    arr = [4, 5, 2, 25]
    next_greater(arr)