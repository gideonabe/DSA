# graph table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

# Parent table
parents = {}
parents["a"] = "start"
parents["fin"] = None

# cost table
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["fin"] = infinity

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
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if n not in costs or new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_cheapest_cost_node(costs)


print("Costs:", costs)
print("Parents", parents)
print("Shortest path cost from start to fin:", costs["fin"])