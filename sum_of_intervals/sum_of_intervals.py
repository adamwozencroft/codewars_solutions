def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    sum = 0
    current_min = intervals[0][0]
    current_max = intervals[0][1]
    
    for i in range(len(intervals)):
        if intervals[i][0] > current_max:
            sum += current_max - current_min
            current_min = intervals[i][0]
            current_max = intervals[i][1]
        else:
            current_max = max(current_max,intervals[i][1])
    sum += current_max-current_min
    
    return sum