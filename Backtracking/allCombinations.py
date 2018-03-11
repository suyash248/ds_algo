from Array import empty_1d_array


# Time Complexity: O(2^n)
def all_combinations(input_seq, combinations):
    for elt in input_seq:
        comb_len = len(combinations)
        for si in xrange(0, comb_len):
            combinations.append(combinations[si] + elt)


"""
                        {}
                a                {}
          ab          a       b      {}
      abc    ab    ac   a  bc   b  c    {}

"""
# Time Complexity: O(2^n)
def all_combinations_v2(input_seq, res, level):
    if level == len(input_seq):
        all_combinations_v2.combinations.add(res)
        return
    all_combinations_v2(input_seq, res, level + 1)
    all_combinations_v2(input_seq, res+input_seq[level], level + 1)


# This solution takes care of duplicates as well.
# https://www.youtube.com/watch?v=xTNFs5KRV_g
# Time Complexity: O(2^n)
def all_combinations_v3(input_seq, count, pos, combinations, level):
    # print till pos
    print_till_pos(combinations, level)

    for i in xrange(pos, len(input_seq)):
        if count[i] == 0:
            continue
        combinations[level] = input_seq[i]
        count[i] -= 1
        all_combinations_v3(input_seq, count, i, combinations, level+1)
        count[i] += 1


def print_till_pos(arr, pos):
    res = ""
    for elt in arr[:pos]:
        res += elt
    print res,


if __name__ == '__main__':
    input_seq = "aabc"

    print "\n------------------- Using V1 -------------------\n"
    combinations = [""] # empty list
    all_combinations(input_seq, combinations)
    print "All the combinations of {} are -\n".format(input_seq), ' '.join(combinations)

    print "\n------------------- Using V2 -------------------\n"
    all_combinations_v2.combinations = set()
    all_combinations_v2(input_seq, "", 0)
    print "All the combinations of {} are - ".format(input_seq)
    for c in all_combinations_v2.combinations: print c,
    print ""

    print "\n------------------- Using V3 -------------------\n"
    ch_counts = {ch: input_seq.count(ch) for ch in input_seq}
    print "All the combinations of {} are - ".format(input_seq)
    all_combinations_v3(ch_counts.keys(), ch_counts.values(), 0, empty_1d_array(len(input_seq)), 0)
