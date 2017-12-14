from Queue import Queue

"""
PROBLEM STATEMENT: 
    There is queue of villager(s) for filling the buckets of water. In one iteration/pass villager can fill exactly
    1 bucket and if a villager requires more than 1 bucket of water then he has to again stand in queue at last position.
    So if a villager requires 'X' bucket of water then it will take 'X' iteration for him.
    Note: Once a villager's requirement is fullfilled, he moves out of the queue. 
    Input: 
        'N' - Number of villagers
        'K' - Number of buckets after which queue status to be calculated.
        Requirements of each villager as comma-separated values. (N values)
        
    Output:
        Queue status(position of villagers) after 'K' buckets are filled. Print -1 if queue becomes empty.
    
    Sample:
        Input: 
            4
            4
            1,2,2,1
        Output:
            2 3
"""

def get_queue_status(req_arr, k):
    q = Queue()
    for p_num in xrange(1, len(req_arr)+1): q.put(p_num)
    while k>0:
        if q.empty():
            break

        person_num = q.get()
        person_capacity = req_arr[person_num - 1]
        req_arr[person_num - 1] = person_capacity - 1
        if req_arr[person_num - 1] > 0:
            q.put(person_num)

        k -= 1
    return q

if __name__ == "__main__":
    n = input("Number of villager(s). N = ")
    k = input("To get the status of queue after 'K' buckets are filled. K = ")
    req_arr = raw_input("Requirements of each 'N' villager, comma-separated = ")
    req_arr = map(lambda s: int(s.strip()), req_arr.split(","))
    q = get_queue_status(req_arr, k)
    # q = get_queue_status([1,2,2,1], 4)

    if q.empty():
        print -1
    else:
        while not q.empty():
            print q.get(),