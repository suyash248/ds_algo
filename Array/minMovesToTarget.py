from Array import MAX

# https://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/
def min_moves_to_reach_target(target, source=0, step_index=0):
    if abs(source)  > target:
        return MAX
    if source == target:
        return step_index

    right = min_moves_to_reach_target(target, source + step_index + 1, step_index=step_index+1)
    left = min_moves_to_reach_target(target, source - step_index-1, step_index=step_index+1)

    return min(right, left)

if __name__ == '__main__':
    target = 3
    min_steps = min_moves_to_reach_target(target)
    print "Minimum {} step(s) are required to reach the target {}".format(min_steps, target)