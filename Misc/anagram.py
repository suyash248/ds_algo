__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

# Time complexity: O(n)
# Space complexity: O(n)
def are_anagram(str1, str2):
    if len(str1) != len(str2): return False

    count_arr = [0] * 256
    for s in str1:
        count_arr[ord(s)] += 1

    for s in str2:
        count_arr[ord(s)] -= 1

    for c in count_arr:
        if c!=0: return False
    return True

if __name__ == '__main__':
    str1 = input("Enter first string: ").strip()
    str2 = input("Enter second string: ").strip()

    res = are_anagram(str1, str2)
    print("{} & {} are anagrams? {}".format(str1, str2, res))



