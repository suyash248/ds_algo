def all_combinations(input_seq, combinations):
    for elt in input_seq:
        comb_len = len(combinations)
        for si in xrange(0, comb_len):
            combinations.append(combinations[si] + elt)


if __name__ == '__main__':
    input_seq = "abcd"
    combinations = [""] # empty set
    all_combinations(input_seq, combinations)
    print "All the combinations of {} are -\n".format(input_seq), combinations