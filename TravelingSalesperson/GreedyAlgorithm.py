# Greedy/Nearest Neighbor Algorithm is one of the algorithm used to solve Traveling-salesperson NP-problems, it doesn't give the optimal solution but it gives the best approximated solution

# 1) A postman needs to deliver to 20 homes. He needs to find the shortest route that goes to all 20 homes. Is this an NP-complete problem?

# SOLUTION
import random 

# generate 20x20 matrix
def generate_distance_matrix(n):
  dist_matrix = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(i+1, n):
      dist = random.randint(1, 100)  # random distance between 1 and 100
      dist_matrix[i][j] = dist
      dist_matrix[j][i] = dist  # symmetric
  return dist_matrix

def nearest_neighbor_tsp(dist_matrix, start=0):
  n = len(dist_matrix)
  visited = [False] * n
  tour = [start]
  total_distance = 0
  current = start
  visited[current] = True

  for _ in range(n - 1):
    # using the underscore(_) means we are not using the loop variable in the loop, we just want to loop (n - 1) times
    next_city = None
    min_dist = float('inf')
    for city in range(n):
      if not visited[city] and dist_matrix[current][city] < min_dist:
        min_dist = dist_matrix[current][city]
        next_city = city
    tour.append(next_city)
    visited[next_city] = True
    total_distance += min_dist
    current = next_city

  # Return to starting city
  total_distance += dist_matrix[current][start]
  tour.append(start)

  return tour, total_distance


# dist_matrix = [
#   [0, 10, 15, 20],
#   [10, 0, 35, 25],
#   [15, 35, 0, 30],
#   [20, 25, 30, 0]
# ]

dist_matrix = generate_distance_matrix(20)

tour, cost = nearest_neighbor_tsp(dist_matrix)
print("Tour:", tour)
print("Total distance:", cost)
