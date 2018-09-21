from copy import copy

def cellCompete(states, days):
    n = len(states)
    nextStates = [-1] * n

    while (days > 0):
        nextStates[0] = states[1]
        nextStates[n - 1] = states[n - 2]
        i = 0
        j = 1
        for k in range(2, n):
            nextStates[j] = 0 if states[i] == states[k] else 1
            i, j = j, k
        days -= 1
        print(nextStates)
        states = copy(nextStates)
    return nextStates

if __name__ == '__main__':
    # states = [1, 0, 0, 0, 0, 1, 0, 0 ]; days = 1;
    states = [1, 1, 1, 0, 1, 1, 1, 1 ]; days = 2
    print(cellCompete(states, days))

