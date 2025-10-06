# graph table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


# to keep track of processed nodes
processed = []

def find_cheapest_cost_node(costs):
  cheapest_cost = float("inf")
  cheapest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cheapest_cost > cost and node not in processed:
      cheapest_cost = cost
      cheapest_cost_node = node
  return cheapest_cost_node

node = find_cheapest_cost_node(costs)
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_cheapest_cost_node(costs)

print("Costs:", costs)
print("Parents", parents)