from Array import empty_1d_array

# Time complexity: O(n^2)
def accomodate_trains(arrival_departure_times):
    #       0           1               2           3             4            5
    # [(915, 956), (1000, 1030), (900, 1045), (1200, 1400), (1420, 1445), (1500, 1510)]
    # 1, 2
    # 1, 4
    # 1, 5
    # 1, 6

    n = len(arrival_departure_times)
    platforms = {}
    platforms_count = empty_1d_array(n, fill_default=0)
    max_overlaps = 0
    # For every i, j will go till i
    for i in range(1, n):
        number_of_overlaps = 0
        for j in range(0, i):
            i_start_time = arrival_departure_times[i][0]
            i_end_time = arrival_departure_times[i][1]
            j_start_time = arrival_departure_times[j][0]
            j_end_time = arrival_departure_times[j][1]

            if j_end_time <= i_start_time:  # Means we can combine these train and assign common platform for them
                number_of_overlaps += 1
                max_overlaps = max(max_overlaps, number_of_overlaps)
                platforms_count[i] += 1
                if j not in platforms:
                    platforms[j] = {i}
                else:
                    platforms[j].add(i)
    print platforms
    print platforms_count
    print max_overlaps

def sort_by_end_time(t1, t2):
    e1 = t1[1]
    e2 = t2[1]

    if e1 < e2:
        return -1
    elif e1 > e2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # List1 = list of arrival time of trains    10:00, 09:00, 09:15, 14:30, 15:00, 12:00
    # List2 = List of departure times of trains 10:30, 10:45, 09:56, 14:45, 15:10, 14:00
    # arrival_departure_times = [(1000, 1030), (900, 1045), (915, 956), (1420, 1445), (1500, 1510), (1200, 1400)] # start, end
    arrival_departure_times = [(900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
    arrival_departure_times.sort(cmp=sort_by_end_time)
    accomodate_trains(arrival_departure_times)