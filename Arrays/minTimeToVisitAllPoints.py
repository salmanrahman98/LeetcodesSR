# https://leetcode.com/problems/minimum-time-visiting-all-points/
def minTimeToVisitAllPoints(points):
    # O(n^2) solution
    count = 0

    i = points[0][0]
    j = points[0][1]
    print(i)
    print(j)
    path_array = []
    path_array.append([i, j])
    print(path_array)
    # looping through array but from 1st position
    for target_arr in points[1:]:
        while True:
            if target_arr[0] > i:
                i += 1
            elif target_arr[0] < i:
                i -= 1

            if target_arr[1] > j:
                j += 1
            elif target_arr[1] < j:
                j -= 1

            path_array.append([i, j])

            if [i, j] == target_arr:
                break

    # using path to calculate the shortest time
    x1, y1 = path_array.pop(0)
    print(path_array)
    print(f"{x1},{y1}")
    return len(path_array)-1


input_points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(input_points))
