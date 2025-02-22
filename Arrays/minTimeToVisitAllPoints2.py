# https://leetcode.com/problems/minimum-time-visiting-all-points/
# O(n) solution
def minTimeToVisitAllPoints(points):
    count = 0

    i = points[0][0]
    j = points[0][1]

    # looping through array but from 1st position
    for target_arr in points[1:]:

        x_axis_distance = abs(i - target_arr[0])
        y_axis_distance = abs(j - target_arr[1])

        if x_axis_distance >= y_axis_distance:
            count += x_axis_distance
        else:
            count += y_axis_distance

        i = target_arr[0]
        j = target_arr[1]

    return count


input_points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(input_points))
