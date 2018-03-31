def accomodate(arrivals, departures):
    arrivals.sort()
    departures.sort()

    arrivals_count = 0
    result = 0
    n = len(arrivals) # + len(departures)

    arr_i = dep_i = 0

    while arr_i < n and dep_i < n:
        if arrivals[arr_i] < departures[dep_i]:
            arrivals_count += 1
            arr_i += 1
            if arrivals_count > result:
                result = arrivals_count
        else:
            arrivals_count -= 1
            dep_i += 1
    return result


if __name__ == '__main__':
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    min_platforms = accomodate(arrivals, departures)
    print "At least {} platform(s) are needed to accomodate all the trains".format(min_platforms)