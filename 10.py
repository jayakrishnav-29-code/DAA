
import math

# Calculate distance
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


# Brute Force
def brute_force(points):
    min_dist = float('inf')
    pair = None

    for i in range(len(points)):
        for j in range(i+1, len(points)):

            d = distance(points[i], points[j])

            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


# Divide and Conquer
def closest_pair(points):

    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2

    left = points[:mid]
    right = points[mid:]

    pair1, d1 = closest_pair(left)
    pair2, d2 = closest_pair(right)

    if d1 < d2:
        min_pair = pair1
        min_dist = d1
    else:
        min_pair = pair2
        min_dist = d2

    mid_x = points[mid][0]

    strip = []

    for p in points:
        if abs(p[0] - mid_x) < min_dist:
            strip.append(p)

    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):

            if strip[j][1] - strip[i][1] >= min_dist:
                break

            d = distance(strip[i], strip[j])

            if d < min_dist:
                min_dist = d
                min_pair = (strip[i], strip[j])

    return min_pair, min_dist


# Main Program
points = [
    (2, 3), (12, 30), (40, 50), (5, 1),
    (12, 10), (3, 4), (8, 7), (9, 8)
]

points.sort(key=lambda p: p[0])

pair, min_dist = closest_pair(points)

print("Given Points:", points)
print("Closest Pair:", pair)
print("Minimum Distance:", round(min_dist, 4))
