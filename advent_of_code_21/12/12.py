from collections import defaultdict

def get_input(filename):
    with open(filename, "r") as file:
        raw_data = file.read()
        graph = defaultdict(list)
        for row in raw_data.split("\n"):
            u, v = row.split('-')
            graph[u].append(v)
            graph[v].append(u)
        return graph

GRAPH = get_input("input.txt")

# recursive function nice and easy recursive function from @michaeljgallagher
# should look up recursion again :D recursive solutions are way better than iterative solutions

def dfs(node, seen, two=False):
    if node == 'end':
        return 1
    if node == 'start' and node in seen:
        return 0
    if node.islower() and node in seen:
        if two:
            two = False
        else:
            return 0
    seen = seen | set({node})
    return sum(dfs(nei, seen, two) for nei in GRAPH[node])

def part_one():
    return dfs('start', set())

def part_two():
    return dfs('start', set(), True)

print(f"Part 1: {part_one()}") 
print(f"Part 2: {part_two()}")  