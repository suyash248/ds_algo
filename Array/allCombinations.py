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
def all_combinations_v2(input_seq, res, level):
    if level == len(input_seq):
        print res,
        return
    all_combinations_v2(input_seq, res, level + 1)
    all_combinations_v2(input_seq, res+input_seq[level], level + 1)

if __name__ == '__main__':
    input_seq = "abc"
    combinations = [""] # empty list
    all_combinations(input_seq, combinations)
    print "All the combinations of {} are -\n".format(input_seq), combinations

    print "All the combinations of {} are -\n".format(input_seq)
    all_combinations_v2(input_seq, "", 0)