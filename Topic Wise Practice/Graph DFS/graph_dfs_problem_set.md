# Graph DFS Practice

Graph DFS differs from tree DFS in key ways:
- **Cycles:** Graphs can have cycles, so you need a `visited` set
- **Multiple components:** Graph may be disconnected
- **Multiple paths:** Same node can be reached different ways

**Core Pattern:**
```cpp
void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
    visited[node] = true;
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph, visited);
        }
    }
}
```

---

## Part 1: Basic Graph Traversal

### Problem 1: Find if Path Exists in Graph

Given n nodes (0 to n-1) and edges, determine if there's a path from source to destination.

```
n = 3, edges = [[0,1], [1,2], [2,0]]
source = 0, destination = 2

has_path(n, edges, 0, 2) → True
```

```
n = 6, edges = [[0,1], [0,2], [3,5], [5,4], [4,3]]
source = 0, destination = 5

has_path(n, edges, 0, 5) → False   # Different components
```

---

### Problem 2: All Paths From Source to Target

Find all paths from node 0 to node n-1 in a **DAG** (directed acyclic graph).

```
graph = [[1,2], [3], [3], []]
# 0 → 1, 0 → 2, 1 → 3, 2 → 3

all_paths(graph) → [[0,1,3], [0,2,3]]
```

```
graph = [[4,3,1], [3,2,4], [3], [4], []]

all_paths(graph) → [[0,4], [0,3,4], [0,1,3,4], [0,1,2,3,4], [0,1,4]]
```

---

### Problem 3: Clone Graph

Deep copy a graph. Each node has a value and a list of neighbors.

```
Input: Node 1 connected to [2, 4]
       Node 2 connected to [1, 3]
       Node 3 connected to [2, 4]
       Node 4 connected to [1, 3]

Output: New graph with same structure
```

**Pattern:** Use a hashmap to track {original node → cloned node}.

---

### Problem 4: Keys and Rooms

n rooms (0 to n-1), room 0 is unlocked. Each room has keys to other rooms. Can you visit all rooms?

```
rooms = [[1], [2], [3], []]

can_visit_all(rooms) → True
# Start at 0 → get key to 1 → get key to 2 → get key to 3
```

```
rooms = [[1,3], [3,0,1], [2], [0]]

can_visit_all(rooms) → False   # Can't reach room 2
```

---

### Problem 5: Find the Town Judge

n people, one might be the judge. The judge trusts nobody, everyone else trusts the judge. Find the judge or return -1.

```
n = 3, trust = [[1,3], [2,3]]

find_judge(n, trust) → 3
```

```
n = 3, trust = [[1,3], [2,3], [3,1]]

find_judge(n, trust) → -1   # 3 trusts 1, so 3 is not judge
```

---

## Part 2: Connected Components

### Problem 6: Number of Connected Components

Count connected components in an undirected graph.

```
n = 5, edges = [[0,1], [1,2], [3,4]]

count_components(n, edges) → 2
# Component 1: {0, 1, 2}
# Component 2: {3, 4}
```

**Pattern:** DFS from each unvisited node, increment count.

---

### Problem 7: Number of Provinces

n cities, isConnected[i][j] = 1 means cities i and j are connected. Count provinces (groups of connected cities).

```
isConnected = [[1,1,0], [1,1,0], [0,0,1]]

find_provinces(isConnected) → 2
# Province 1: cities 0, 1
# Province 2: city 2
```

---

### Problem 8: Number of Islands

Count islands in a 2D grid ('1' = land, '0' = water).

```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

num_islands(grid) → 3
```

**Pattern:** DFS from each unvisited '1', mark visited cells.

---

### Problem 9: Max Area of Island

Find the largest island (connected 1s) by area.

```
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

max_area(grid) → 6
```

---

### Problem 10: Island Perimeter

Find the perimeter of the single island.

```
grid = [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]

island_perimeter(grid) → 16
```

---

### Problem 11: Number of Closed Islands

Count islands completely surrounded by water (not touching the boundary).

```
grid = [
  [1,1,1,1,1,1,1,0],
  [1,0,0,0,0,1,1,0],
  [1,0,1,0,1,1,1,0],
  [1,0,0,0,0,1,0,1],
  [1,1,1,1,1,1,1,0]
]

closed_islands(grid) → 2
```

**Hint:** First mark all boundary-connected land, then count remaining islands.

---

### Problem 12: Number of Enclaves

Count land cells that cannot walk off the boundary.

```
grid = [
  [0,0,0,0],
  [1,0,1,0],
  [0,1,1,0],
  [0,0,0,0]
]

num_enclaves(grid) → 3
```

---

### Problem 13: Making A Large Island

You can change at most one 0 to 1. Find the largest island possible.

```
grid = [[1,0], [0,1]]

largest_island(grid) → 3   # Change grid[0][1] or grid[1][0]
```

---

## Part 3: Cycle Detection

### Problem 14: Course Schedule (Cycle in Directed Graph)

n courses with prerequisites. Check if you can finish all courses (no circular dependency).

```
numCourses = 2, prerequisites = [[1,0]]
# Course 1 requires course 0

can_finish(2, [[1,0]]) → True
can_finish(2, [[1,0], [0,1]]) → False   # Cycle: 0 ↔ 1
```

**Pattern:** DFS with three states: unvisited, visiting (in current path), visited.

```cpp
// 0 = unvisited, 1 = visiting, 2 = visited
bool hasCycle(int node, vector<vector<int>>& graph, vector<int>& state) {
    state[node] = 1;  // visiting
    
    for (int neighbor : graph[node]) {
        if (state[neighbor] == 1) return true;  // cycle!
        if (state[neighbor] == 0 && hasCycle(neighbor, graph, state)) {
            return true;
        }
    }
    
    state[node] = 2;  // visited
    return false;
}
```

---

### Problem 15: Course Schedule II (Topological Sort)

Return a valid order to take all courses, or empty if impossible.

```
numCourses = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]

find_order(4, prerequisites) → [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

### Problem 16: Graph Valid Tree

Check if n nodes with given edges form a valid tree (connected, no cycles).

```
n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]

valid_tree(5, edges) → True
```

```
n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

valid_tree(5, edges) → False   # Has cycle
```

**Tree conditions:** Connected AND (n-1 edges OR no cycle).

---

### Problem 17: Detect Cycle in Undirected Graph

Check if an undirected graph has a cycle.

```
n = 4, edges = [[0,1], [1,2], [2,3]]
has_cycle(n, edges) → False

n = 4, edges = [[0,1], [1,2], [2,3], [3,0]]
has_cycle(n, edges) → True
```

**Pattern:** Track parent to avoid false positive from going back.

---

### Problem 18: Redundant Connection

Find the edge that, if removed, makes the graph a tree (no cycle).

```
edges = [[1,2], [1,3], [2,3]]

find_redundant(edges) → [2, 3]   # Removing this breaks the cycle
```

---

### Problem 19: Redundant Connection II (Directed Graph)

In a directed graph that should be a rooted tree, find the edge causing the issue.

```
edges = [[1,2], [1,3], [2,3]]

find_redundant_directed(edges) → [2, 3]
```

---

## Part 4: Grid DFS Problems

### Problem 20: Flood Fill

Starting from (sr, sc), change all connected cells of the same color to newColor.

```
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2

flood_fill(image, 1, 1, 2) → [[2,2,2],[2,2,0],[2,0,1]]
```

---

### Problem 21: Surrounded Regions

Capture all 'O's surrounded by 'X's (flip to 'X'). 'O's on the border are not captured.

```
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

solve(board) →

[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

**Pattern:** Mark border-connected 'O's first, then flip remaining 'O's.

---

### Problem 22: Pacific Atlantic Water Flow

Water can flow to Pacific (top/left) or Atlantic (bottom/right) if the path is non-increasing. Find cells that can reach both oceans.

```
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]

pacific_atlantic(heights) → [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Pattern:** DFS from ocean boundaries inward (reverse the flow direction).

---

### Problem 23: Word Search

Check if a word exists in a grid (adjacent cells, each cell used once).

```
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exist(board, "ABCCED") → True
exist(board, "SEE") → True
exist(board, "ABCB") → False
```

---

### Problem 24: Word Search II

Find all words from a list that exist in the grid.

```
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

find_words(board, words) → ["eat", "oath"]
```

**Hint:** Use Trie for efficient prefix matching.

---

### Problem 25: Longest Increasing Path in a Matrix

Find the longest strictly increasing path.

```
matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

longest_path(matrix) → 4   # Path: 1 → 2 → 6 → 9
```

**Pattern:** DFS with memoization.

---

### Problem 26: Unique Paths III

Grid with 1 (start), 2 (end), 0 (empty), -1 (obstacle). Count paths from start to end visiting every empty cell exactly once.

```
grid = [
  [1,0,0,0],
  [0,0,0,0],
  [0,0,2,-1]
]

unique_paths(grid) → 2
```

---

### Problem 27: Robot Room Cleaner

Clean all reachable cells with a robot that can only move(), turnLeft(), turnRight(), and clean(). You don't know the grid.

```
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
]
```

**Pattern:** DFS with relative directions, backtracking.

---

## Part 5: Topological Sort

### Problem 28: Alien Dictionary

Given sorted words in an alien language, derive the character order.

```
words = ["wrt","wrf","er","ett","rftt"]

alien_order(words) → "wertf"
```

```
words = ["z","x"]

alien_order(words) → "zx"
```

**Pattern:** Build graph from adjacent word pairs, then topological sort.

---

### Problem 29: Sequence Reconstruction

Check if a sequence is the only shortest supersequence of given subsequences.

```
nums = [1,2,3], sequences = [[1,2],[1,3]]

sequence_reconstruction(nums, sequences) → False
# [1,3,2] is also valid
```

```
nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]

sequence_reconstruction(nums, sequences) → True
```

---

### Problem 30: Parallel Courses

n courses, prerequisites given. Return minimum semesters to take all courses (unlimited courses per semester if no dependency). Return -1 if impossible.

```
n = 3, relations = [[1,3],[2,3]]

minimum_semesters(n, relations) → 2
# Semester 1: courses 1, 2
# Semester 2: course 3
```

---

### Problem 31: Sort Items by Groups Respecting Dependencies

Items belong to groups. Items in same group must be adjacent. Respect item dependencies. Return valid ordering.

```
n = 8, m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

sort_items(...) → [6,3,4,1,5,2,0,7]  # One valid answer
```

---

## Part 6: Path Finding and Connectivity

### Problem 32: Path with Maximum Probability

Find path from start to end with maximum probability of success.

```
n = 3
edges = [[0,1],[1,2],[0,2]]
probs = [0.5, 0.5, 0.2]
start = 0, end = 2

max_probability(...) → 0.25   # 0.5 * 0.5 via path 0→1→2
```

---

### Problem 33: Evaluate Division

Given equations a/b = k, answer queries x/y.

```
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

calc_equation(...) → [6.0, 0.5, -1.0, 1.0, -1.0]
```

**Pattern:** Build weighted graph, DFS to find path and multiply weights.

---

### Problem 34: Accounts Merge

Merge accounts with common emails.

```
accounts = [
  ["John","john@mail.com","john_newyork@mail.com"],
  ["John","john@mail.com","john00@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnny@mail.com"]
]

accounts_merge(accounts) → [
  ["John","john00@mail.com","john@mail.com","john_newyork@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnny@mail.com"]
]
```

---

### Problem 35: Similar String Groups

Two strings are similar if swapping two letters makes them equal. Count groups of similar strings.

```
strs = ["tars","rats","arts","star"]

num_similar_groups(strs) → 2
# Group 1: "tars", "rats", "arts"
# Group 2: "star"
```

---

### Problem 36: Reorder Routes to Make All Paths Lead to City Zero

Directed roads. Reorder minimum roads so all cities can reach city 0.

```
n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

min_reorder(n, connections) → 3
```

---

## Part 7: Bipartite and Coloring

### Problem 37: Is Graph Bipartite?

Check if graph can be 2-colored (no adjacent nodes have same color).

```
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

is_bipartite(graph) → False
```

```
graph = [[1,3],[0,2],[1,3],[0,2]]

is_bipartite(graph) → True
```

**Pattern:** DFS/BFS with two colors. If neighbor has same color, not bipartite.

---

### Problem 38: Possible Bipartition

n people, some dislike each other. Can we split into two groups where no one is with someone they dislike?

```
n = 4, dislikes = [[1,2],[1,3],[2,4]]

possible_bipartition(n, dislikes) → True
# Group 1: {1, 4}, Group 2: {2, 3}
```

---

### Problem 39: Flower Planting With No Adjacent

n gardens connected by paths. Plant flowers (1-4) so no adjacent gardens have the same flower.

```
n = 3, paths = [[1,2],[2,3],[3,1]]

garden_no_adj(n, paths) → [1, 2, 3]
```

---

## Part 8: Advanced Graph DFS

### Problem 40: Critical Connections in a Network

Find all edges whose removal disconnects the graph (bridges).

```
n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]

critical_connections(n, connections) → [[1, 3]]
```

**Pattern:** Tarjan's algorithm with discovery time and low-link values.

---

### Problem 41: Minimum Height Trees

Find nodes that, if used as root, give minimum height tree.

```
n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

find_min_height_trees(n, edges) → [3, 4]
```

**Hint:** Repeatedly remove leaf nodes. Remaining 1-2 nodes are centers.

---

### Problem 42: Find Eventual Safe States

Find all nodes that eventually lead to a terminal node (no outgoing edges) regardless of path taken.

```
graph = [[1,2],[2,3],[5],[0],[5],[],[]]

eventual_safe_nodes(graph) → [2, 4, 5, 6]
```

---

### Problem 43: Loud and Rich

Given richer[i] = [a, b] means a is richer than b, and quiet[i] is quietness of person i. For each person, find the quietest person who is at least as rich.

```
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]

loud_and_rich(richer, quiet) → [5,5,2,5,4,5,6,7]
```

---

### Problem 44: Time Needed to Inform All Employees

Tree structure of employees. Find time to inform all employees starting from head.

```
n = 6, headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]

num_of_minutes(...) → 1
```

---

### Problem 45: Sum of Distances in Tree

For each node, find sum of distances to all other nodes.

```
n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

sum_of_distances(n, edges) → [8,12,6,10,10,10]
```

**Pattern:** Two DFS passes - one to compute subtree sizes, one to compute answers.

---

## Strategies and Patterns

### Basic Graph DFS Template

```cpp
void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
    visited[node] = true;
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph, visited);
        }
    }
}

// Call for all components
for (int i = 0; i < n; i++) {
    if (!visited[i]) {
        dfs(i, graph, visited);
        componentCount++;
    }
}
```

### Cycle Detection in Directed Graph

```cpp
// 0 = unvisited, 1 = visiting (in stack), 2 = visited
bool hasCycle(int node, vector<vector<int>>& graph, vector<int>& state) {
    state[node] = 1;
    
    for (int neighbor : graph[node]) {
        if (state[neighbor] == 1) return true;   // back edge = cycle
        if (state[neighbor] == 0) {
            if (hasCycle(neighbor, graph, state)) return true;
        }
    }
    
    state[node] = 2;
    return false;
}
```

### Cycle Detection in Undirected Graph

```cpp
bool hasCycle(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited) {
    visited[node] = true;
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            if (hasCycle(neighbor, node, graph, visited)) return true;
        } else if (neighbor != parent) {
            return true;  // visited and not parent = cycle
        }
    }
    return false;
}
```

### Grid DFS Template

```cpp
int directions[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

void dfs(int r, int c, vector<vector<int>>& grid) {
    if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size()) return;
    if (grid[r][c] == 0) return;  // water or visited
    
    grid[r][c] = 0;  // mark visited
    
    for (auto& dir : directions) {
        dfs(r + dir[0], c + dir[1], grid);
    }
}
```

### Topological Sort with DFS

```cpp
void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited, stack<int>& result) {
    visited[node] = true;
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph, visited, result);
        }
    }
    
    result.push(node);  // add after all descendants
}

// Pop stack for topological order
```

### Common Patterns Summary

| Pattern | Use Case |
|---------|----------|
| Basic DFS + visited | Traversal, connectivity |
| DFS + component count | Number of islands, provinces |
| DFS + path tracking | All paths, backtracking |
| Three-state DFS | Cycle detection in directed graph |
| DFS + parent tracking | Cycle detection in undirected graph |
| DFS + memoization | Longest path, counting paths |
| DFS from boundaries | Surrounded regions, ocean flow |
| Topological DFS | Course schedule, alien dictionary |
| Bipartite DFS | 2-coloring, possible bipartition |

### Graph vs Tree DFS

| Aspect | Tree DFS | Graph DFS |
|--------|----------|-----------|
| Visited set | Not needed | Required |
| Cycles | None | Must handle |
| Starting point | Root | Any node (may need all) |
| Components | One | May be multiple |
| Path uniqueness | One path to each node | Multiple paths possible |

### Edge Cases

1. **Empty graph** (n = 0)
2. **Disconnected graph** (multiple components)
3. **Self-loops**
4. **Parallel edges** (multiple edges between same nodes)
5. **Single node**
6. **Fully connected graph**
7. **No edges**

---

Good luck! Start with Part 1-2 for basic traversal and components. Part 3 (cycle detection) and Part 5 (topological sort) are essential patterns. Grid problems in Part 4 are very common in interviews.
