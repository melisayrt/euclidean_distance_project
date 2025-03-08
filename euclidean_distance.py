import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


points = [(1, 2), (4, 6), (8, 3), (5, 9)]


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)


print("Minimum Öklid Mesafesi:", min(distances))
