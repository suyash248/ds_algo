from Array import empty_1d_array

def schedule_jobs(job_durations_profits):
    profits = [e[2] for e in job_durations_profits]
    # For every `i`, `j` will go up to `i`(excluding).
    for i in range(1, len(profits)):
        for j in range(0, i):
            i_start_time = job_durations_profits[i][0]
            i_end_time = job_durations_profits[i][1]
            i_profit = job_durations_profits[i][2]

            j_start_time = job_durations_profits[j][0]
            j_end_time = job_durations_profits[j][1]
            j_profit = job_durations_profits[j][2]

            # Checking if `j`th job ends before `i`th job
            if j_end_time <= i_start_time:
                profits[i] = max(profits[i], i_profit + j_profit)
    return max(profits)

def sort_by_end_time(e1, e2):
    end_time1 = e1[1]
    end_time2 = e2[1]

    if end_time1 > end_time2:
        return 1
    elif end_time1 < end_time2:
        return -1
    return 0

if __name__ == '__main__':
    job_durations_profits = [(1, 4, 3), (4, 7, 2), (2, 6, 5), (7, 10, 8), (6, 8, 6), (5, 9, 4)] # start, end, profit
    job_durations_profits.sort(cmp=sort_by_end_time)
    max_profit = schedule_jobs(job_durations_profits)
    print "Max profit is {}".format(max_profit)

