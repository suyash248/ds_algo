from Array import empty_2d_array


# Time complexity: O(2^n)
def lcs_recursive(p, q, plen, qlen):
    if plen == 0 or qlen == 0:
        return 0

    if p[plen-1] == q[qlen-1]:
        return 1 + lcs_recursive(p, q, plen-1, qlen-1)
    else:
        return max(lcs_recursive(p, q, plen-1, qlen), lcs_recursive(p, q, plen, qlen-1))

"""
         "" a  b  c  d  e  f  g  h
            
    ""   0  0  0  0  0  0  0  0  0
    k    0  0  0  0  0  0  0  0  0
    l    0  0  0  0  0  0  0  0  0
    b    0  0  1  1  1  1  1  1  1
    m    0  0  1  1  1  1  1  1  1
    e    0  0  1  1  1  2  2  2  2
    f    0  0  1  1  1  2  3  3  3
    z    0  0  1  1  1  2  3  3  3
    h    0  0  1  1  1  2  3  3  4
"""
# Time complexity: O(mn), where m, n are lengths of sub-sequences
def lcs_dp(p, q):
    rows = len(p); cols = len(q)
    table = empty_2d_array(rows, cols)

    for row in xrange(0, rows):
        for col in xrange(0, cols):
            if row == 0 or col == 0:        # If either of 2 sequence is empty, lcs is 0.
                table[row][col] = 0
                continue

            if p[row] == q[col]:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = max(table[row-1][col], table[row][col-1])
    return table[rows-1][cols-1]

if __name__ == '__main__':
    p = "abcdefgh"
    q = "klbmefzh"

    print "\n------- Using recursive approach -------\n"
    lcs_len = lcs_recursive(p, q, len(p), len(q))
    print "Length of LCS for sequences '{}' & '{}' is {}".format(p, q, lcs_len)

    print "\n------- Using DP approach -------\n"
    lcs_len = lcs_dp(p, q)
    print "Length of LCS for sequences '{}' & '{}' is {}".format(p, q, lcs_len)