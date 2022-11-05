from typing import List


def ninjaTrainingMemo(day: int, day_points: List[List[int]], last_task: int, dp: List[List[int]]) -> int:
    max_point = 0
    if day == 0:
        for (task, point) in enumerate(day_points[day]):
            if task != last_task:
                max_point = max(max_point, point)
        return max_point

    if dp[day][last_task] != -1:
        return dp[day][last_task]
    for (task, point) in enumerate(day_points[day]):
        if task != last_task:
            curr_point = point + ninjaTrainingMemo(day - 1, day_points, task, dp)
            max_point = max(max_point, curr_point)
    dp[day][last_task] = max_point
    return max_point


def ninjaTrainingTabulation(day: int, day_points: List[List[int]], dp: List[List[int]]) -> int:
    days = len(day_points)
    tasks = len(day_points[0])
    dp = [[-1] * (tasks + 1)] * days
    # TODO


if __name__ == '__main__':
    points = [
        [1, 2, 5],
        [3, 1, 1],
        [3, 3, 3]
    ]
    days = len(points)
    tasks = len(points[0])
    dp = [[-1] * (tasks + 1)] * days
    res = ninjaTrainingMemo(days - 1, points, len(points), dp)
    print(res)
