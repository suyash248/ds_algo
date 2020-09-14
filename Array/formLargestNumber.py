from functools import reduce
def compare(a, b):
    ab = int(a + b)
    ba = int(b + a)
    m = max(ab, ba)
    return str(m)

def form_largest_number(arr):
    arr.sort()
    arr = map(str, arr)

    largest_num = reduce(compare, arr)
    return largest_num

if __name__ == "__main__":
    arr = [250, 74, 659, 931, 273, 545, 879, 924] # 93192487974659545273250
    # arr = [54, 546, 548, 60]
    #arr = [1, 34, 3, 98, 9, 76, 45, 4]
    largest_num = form_largest_number(arr)
    print ("Largest number :", largest_num)
