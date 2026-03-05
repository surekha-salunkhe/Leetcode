# Graph BFS Practice

BFS on graphs explores nodes **level by level** from the source. Key property: **BFS finds the shortest path in unweighted graphs.**

**When to use BFS over DFS:**
- Shortest path in unweighted graph
- Minimum steps/moves/transformations
- Level-by-level exploration needed
- Finding nearest something

**Core Pattern:**
```cpp
int bfs(int start, int target, vector<vector<int>>& graph) {
    queue<int> q;
    unordered_set<int> visited;
    
    q.push(start);
    visited.insert(start);
    int distance = 0;
    
    while (!q.empty()) {
        int levelSize = q.size();
        
        for (int i = 0; i < levelSize; i++) {
            int node = q.front();
            q.pop();
            
            if (node == target) return distance;
            
            for (int neighbor : graph[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        distance++;
    }
    return -1;  // not found
}
```

---

## Part 1: Basic Graph BFS

### Problem 1: Find if Path Exists in Graph

Given n nodes and edges, determine if there's a path from source to destination.

```
n = 3, edges = [[0,1], [1,2], [2,0]]
source = 0, destination = 2

has_path(n, edges, 0, 2) → True
```

---

### Problem 2: Shortest Path in Binary Matrix

Find shortest path from top-left to bottom-right in a binary matrix. Move in 8 directions. 0 = open, 1 = blocked.

```
grid = [
  [0,0,0],
  [1,1,0],
  [1,1,0]
]

shortest_path(grid) → 4
```

```
grid = [[0,1], [1,0]]

shortest_path(grid) → 2
```

---

### Problem 3: Nearest Exit from Entrance in Maze

Find shortest path from entrance to any exit (boundary cell). '+' = wall, '.' = open.

```
maze = [
  ["+","+",".","+"​],
  [".",".",".","+"],
  ["+","+","+","."]
]
entrance = [1, 2]

nearest_exit(maze, entrance) → 1   # Exit at [0,2]
```

---

### Problem 4: Shortest Bridge

Two islands of 1s. Find minimum 0s to flip to connect them.

```
grid = [
  [0,1],
  [1,0]
]

shortest_bridge(grid) → 1
```

```
grid = [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]

shortest_bridge(grid) → 2
```

**Pattern:** DFS to find first island, BFS to expand until hitting second island.

---

### Problem 5: 01 Matrix

For each cell, find distance to nearest 0.

```
mat = [
  [0,0,0],
  [0,1,0],
  [1,1,1]
]

update_matrix(mat) → [
  [0,0,0],
  [0,1,0],
  [1,2,1]
]
```

**Pattern:** Multi-source BFS starting from all 0s simultaneously.

---

### Problem 6: Rotting Oranges

Fresh = 1, rotten = 2, empty = 0. Every minute, fresh oranges adjacent to rotten become rotten. Return minutes until no fresh oranges, or -1 if impossible.

```
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]

oranges_rotting(grid) → 4
```

---

### Problem 7: Walls and Gates

Fill each empty room (INF) with distance to nearest gate (0). -1 = wall.

```
rooms = [
  [INF, -1,  0, INF],
  [INF,INF,INF, -1],
  [INF, -1,INF, -1],
  [  0, -1,INF,INF]
]

walls_and_gates(rooms) →

[
  [3, -1, 0,  1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3,  4]
]
```

---

### Problem 8: As Far from Land as Possible

Find water cell (0) with maximum distance to any land cell (1). Return that distance.

```
grid = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

max_distance(grid) → 2   # Center cell
```

---

## Part 2: Shortest Path Problems

### Problem 9: Word Ladder

Transform beginWord to endWord, changing one letter at a time. Each intermediate word must be in wordList. Return minimum transformations.

```
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

ladder_length("hit", "cog", wordList) → 5
# hit → hot → dot → dog → cog
```

---

### Problem 10: Word Ladder II

Return all shortest transformation sequences.

```
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

find_ladders("hit", "cog", wordList) → [
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```

---

### Problem 11: Minimum Genetic Mutation

Gene string of 8 characters (A, C, G, T). Find minimum mutations from start to end. Each mutation changes one character and must be in bank.

```
start = "AACCGGTT", end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

min_mutation(start, end, bank) → 2
# AACCGGTT → AACCGGTA → AAACGGTA
```

---

### Problem 12: Open the Lock

Lock has 4 wheels (0-9). Start at "0000", target given. Some deadends cause lock to stop. Find minimum turns.

```
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

open_lock(deadends, target) → 6
```

---

### Problem 13: Minimum Knight Moves

On infinite chess board, knight starts at (0,0). Find minimum moves to reach (x,y).

```
min_knight_moves(2, 1) → 1
min_knight_moves(5, 5) → 4
```

---

### Problem 14: Sliding Puzzle

2×3 board with tiles 1-5 and one empty (0). Slide tiles to reach [[1,2,3],[4,5,0]]. Return minimum moves or -1.

```
board = [[1,2,3],[4,0,5]]

sliding_puzzle(board) → 1   # Swap 0 and 5
```

```
board = [[4,1,2],[5,0,3]]

sliding_puzzle(board) → 5
```

---

### Problem 15: Shortest Path to Get All Keys

Grid with start '@', keys 'a'-'f', locks 'A'-'F', walls '#', empty '.'. Find shortest path to collect all keys.

```
grid = [
  "@.a..",
  "###.#",
  "b.A.B"
]

shortest_path_all_keys(grid) → 8
```

**Pattern:** BFS with state = (position, keys_collected).

---

### Problem 16: Bus Routes

Routes[i] is list of stops for bus i. Find minimum buses to go from source to target.

```
routes = [[1,2,7],[3,6,7]]
source = 1, target = 6

num_buses_to_destination(routes, 1, 6) → 2
# Bus 0 from 1→7, Bus 1 from 7→6
```

---

## Part 3: Multi-Source BFS

### Problem 17: Shortest Distance from All Buildings

Find empty land (0) with minimum total distance to all buildings (1). -1 = obstacle.

```
grid = [
  [1,0,2,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]

shortest_distance(grid) → 7   # Cell (1,2)
```

**Pattern:** BFS from each building, sum distances.

---

### Problem 18: Pacific Atlantic Water Flow (BFS approach)

Find cells that can reach both Pacific (top/left) and Atlantic (bottom/right).

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

---

### Problem 19: Map of Highest Peak

Grid with water (1) and land (0). Assign heights to land cells where adjacent cells differ by at most 1. Maximize the maximum height. Water height = 0.

```
isWater = [[0,1],[0,0]]

highest_peak(isWater) → [[1,0],[2,1]]
```

---

### Problem 20: Surrounded Regions (BFS approach)

Capture 'O's surrounded by 'X's.

```
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

solve(board) → all O's become X's except the boundary-connected one
```

---

## Part 4: State-Space BFS

When the "graph" isn't explicit — you explore states and transitions.

### Problem 21: Snakes and Ladders

Board 1 to n². Snakes and ladders teleport you. Roll 1-6 on each turn. Find minimum moves to reach n².

```
board = [
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,35,-1,-1,13,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,15,-1,-1,-1,-1]
]

snakes_and_ladders(board) → 4
```

---

### Problem 22: Minimum Number of Flips to Convert Binary Matrix to Zero

Flip any cell (toggle it and all adjacent cells). Find minimum flips to make all zeros.

```
mat = [[0,0],[0,1]]

min_flips(mat) → 3
```

---

### Problem 23: Shortest Path Visiting All Nodes

Find shortest path that visits all nodes (can revisit nodes).

```
graph = [[1,2,3],[0],[0],[0]]

shortest_path_length(graph) → 4
# Start at 0, visit 1,2,3 → path 0→1→0→2→0→3
```

**State:** (current_node, visited_mask)

---

### Problem 24: Minimum Moves to Reach Target with Rotations

1×2 snake starts horizontal at (0,0)-(0,1). Move to (n-1,n-2)-(n-1,n-1). Can move right, down, rotate.

```
grid = [
  [0,0,0,0,0,1],
  [1,1,0,0,1,0],
  [0,0,0,0,1,1],
  [0,0,1,0,1,0],
  [0,1,1,0,0,0],
  [0,1,1,0,0,0]
]

minimum_moves(grid) → 11
```

---

### Problem 25: Escape a Large Maze

Infinite grid with some blocked cells. Check if you can reach target from source.

```
blocked = [[0,1],[1,0]]
source = [0,0], target = [0,2]

is_escape_possible(blocked, source, target) → False
```

**Hint:** Limited BFS — if you escape the "trapped area" (bounded by blocked cells), you're free.

---

### Problem 26: Cut Off Trees for Golf Event

Grid of tree heights. Cut trees in order of height (shortest first). Find minimum steps to cut all trees, starting from (0,0).

```
forest = [
  [1,2,3],
  [0,0,4],
  [7,6,5]
]

cut_off_tree(forest) → 6
```

---

## Part 5: Weighted Shortest Path (0-1 BFS)

For graphs with edge weights 0 and 1 only, use deque: add 0-weight neighbors to front, 1-weight to back.

### Problem 27: Minimum Cost to Make at Least One Valid Path in a Grid

Grid with arrows (1=right, 2=left, 3=down, 4=up). Following arrow = cost 0, changing = cost 1. Find minimum cost from (0,0) to (n-1,m-1).

```
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

min_cost(grid) → 3
```

---

### Problem 28: Minimum Obstacle Removal to Reach Corner

Grid with 0 (empty) and 1 (obstacle). Cost to remove obstacle = 1. Find minimum removals to reach (n-1,m-1).

```
grid = [
  [0,1,1],
  [1,1,0],
  [1,1,0]
]

minimum_obstacles(grid) → 2
```

---

### Problem 29: Minimum Cost to Reach Destination in Time

Cities connected by roads with time. Each city has passing fee. Find minimum cost to reach destination within maxTime.

```
maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]

min_cost(maxTime, edges, passingFees) → 11   # Path 0→1→2→5
```

---

## Part 6: Grid BFS Problems

### Problem 30: Shortest Path in a Grid with Obstacles Elimination

Find shortest path from (0,0) to (m-1,n-1). Can eliminate at most k obstacles.

```
grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0],
  [0,1,1],
  [0,0,0]
]
k = 1

shortest_path(grid, k) → 6
```

**State:** (row, col, obstacles_remaining)

---

### Problem 31: Shortest Path with Alternating Colors

Graph with red and blue edges. Find shortest path from 0 to each node, alternating colors.

```
n = 3
red_edges = [[0,1],[1,2]]
blue_edges = []

shortest_alternating_paths(n, red_edges, blue_edges) → [0,1,-1]
```

---

### Problem 32: Minimum Jumps to Reach Home

Bug starts at 0, wants to reach x. Can jump forward a or backward b (but not twice backward in a row). Some positions are forbidden.

```
forbidden = [14,4,18,1,15]
a = 3, b = 15, x = 9

minimum_jumps(forbidden, a, b, x) → 3
```

---

### Problem 33: Jump Game III

Array of non-negative integers. From index i, jump to i+arr[i] or i-arr[i]. Check if you can reach any index with value 0.

```
arr = [4,2,3,0,3,1,2], start = 5

can_reach(arr, start) → True
# 5 → 4 → 1 → 3 (value is 0)
```

---

### Problem 34: Jump Game IV

Array of integers. From index i, jump to i+1, i-1, or any j where arr[j] == arr[i]. Find minimum jumps to reach last index.

```
arr = [100,-23,-23,404,100,23,23,23,3,404]

min_jumps(arr) → 3
# 0 → 4 → 3 → 9
```

---

### Problem 35: Trapping Rain Water II (3D)

2D heightmap. Find how much water it can trap.

```
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

trap_rain_water(heightMap) → 4
```

**Pattern:** BFS from boundaries inward, using min-heap.

---

## Part 7: Bidirectional BFS

Search from both start and end simultaneously. Meets in the middle for huge speedup.

### Problem 36: Word Ladder (Bidirectional)

Same as Problem 9, but use bidirectional BFS for efficiency.

```
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

ladder_length("hit", "cog", wordList) → 5
```

---

### Problem 37: Minimum Genetic Mutation (Bidirectional)

Same as Problem 11 with bidirectional approach.

---

### Problem 38: Open the Lock (Bidirectional)

Same as Problem 12 with bidirectional approach.

---

## Part 8: Advanced BFS

### Problem 39: K-Similar Strings

Two strings are K-similar if we can swap positions in one to get the other in exactly K swaps. Find minimum K.

```
k_similarity("ab", "ba") → 1
k_similarity("abc", "bca") → 2
k_similarity("abac", "baca") → 2
```

---

### Problem 40: Cheapest Flights Within K Stops

Find cheapest flight from src to dst with at most k stops.

```
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0, dst = 3, k = 1

find_cheapest_price(...) → 700   # 0→1→3
```

**Note:** BFS with stops as levels, but need to handle edge weights.

---

### Problem 41: Network Delay Time

Find time for signal to reach all nodes from source k.

```
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4, k = 2

network_delay_time(times, n, k) → 2
```

---

### Problem 42: Reachable Nodes In Subdivided Graph

Edges have counts representing subdivisions. From node 0 with maxMoves, count reachable nodes (including subdivision points).

```
edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6, n = 3

reachable_nodes(edges, maxMoves, n) → 13
```

---

### Problem 43: Frog Position After T Seconds

Tree graph. Frog starts at vertex 1, jumps to random unvisited neighbor each second. Find probability of being at target after exactly t seconds.

```
n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2, target = 4

frog_position(n, edges, t, target) → 0.16666...
```

---

### Problem 44: Second Minimum Time to Reach Destination

n vertices, edges. Traffic light at each vertex changes every `change` minutes. Find second minimum time from 1 to n.

```
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3, change = 5

second_minimum(n, edges, time, change) → 13
```

---

### Problem 45: Minimum Reverse Operations

Array of size n with single 1 at position p, rest are 0s. Can reverse any subarray of length k. Some positions are banned. Find minimum operations to move 1 to each position.

```
n = 4, p = 0, banned = [1,2], k = 4

min_reverse_operations(n, p, banned, k) → [0,-1,-1,1]
```

---

## Strategies and Patterns

### Standard BFS Template

```cpp
int bfs(int start, int target, vector<vector<int>>& graph) {
    queue<int> q;
    unordered_set<int> visited;
    
    q.push(start);
    visited.insert(start);
    int distance = 0;
    
    while (!q.empty()) {
        int levelSize = q.size();
        
        for (int i = 0; i < levelSize; i++) {
            int node = q.front();
            q.pop();
            
            if (node == target) return distance;
            
            for (int neighbor : graph[node]) {
                if (!visited.count(neighbor)) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        distance++;
    }
    return -1;
}
```

### Multi-Source BFS Template

```cpp
// Start BFS from multiple sources simultaneously
queue<pair<int,int>> q;
vector<vector<int>> dist(m, vector<int>(n, INT_MAX));

// Add all sources
for (auto& source : sources) {
    q.push({source.r, source.c});
    dist[source.r][source.c] = 0;
}

while (!q.empty()) {
    auto [r, c] = q.front();
    q.pop();
    
    for (auto& [dr, dc] : directions) {
        int nr = r + dr, nc = c + dc;
        if (valid(nr, nc) && dist[nr][nc] == INT_MAX) {
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }
}
```

### State-Space BFS Template

```cpp
// BFS where state is more than just position
// Example: (position, keys_collected)
queue<tuple<int, int, int>> q;  // (row, col, keys_bitmask)
set<tuple<int,int,int>> visited;

q.push({start_r, start_c, 0});
visited.insert({start_r, start_c, 0});

while (!q.empty()) {
    auto [r, c, keys] = q.front();
    q.pop();
    
    if (keys == all_keys) return distance;
    
    for (each neighbor) {
        int new_keys = keys;
        if (is_key) new_keys |= (1 << key_id);
        if (is_lock && !(keys & (1 << lock_id))) continue;
        
        if (!visited.count({nr, nc, new_keys})) {
            visited.insert({nr, nc, new_keys});
            q.push({nr, nc, new_keys});
        }
    }
}
```

### 0-1 BFS Template

```cpp
// For graphs with edge weights 0 and 1 only
deque<int> dq;
vector<int> dist(n, INT_MAX);

dq.push_back(start);
dist[start] = 0;

while (!dq.empty()) {
    int node = dq.front();
    dq.pop_front();
    
    for (auto [neighbor, weight] : graph[node]) {
        if (dist[node] + weight < dist[neighbor]) {
            dist[neighbor] = dist[node] + weight;
            if (weight == 0) {
                dq.push_front(neighbor);  // 0-weight to front
            } else {
                dq.push_back(neighbor);   // 1-weight to back
            }
        }
    }
}
```

### Bidirectional BFS Template

```cpp
unordered_set<string> front, back, visited;
front.insert(start);
back.insert(target);
int steps = 0;

while (!front.empty() && !back.empty()) {
    // Always expand smaller set
    if (front.size() > back.size()) swap(front, back);
    
    unordered_set<string> next;
    for (string& word : front) {
        for (string& neighbor : getNeighbors(word)) {
            if (back.count(neighbor)) return steps + 1;
            if (!visited.count(neighbor)) {
                visited.insert(neighbor);
                next.insert(neighbor);
            }
        }
    }
    front = next;
    steps++;
}
return -1;
```

### When to Use BFS vs DFS

| Use BFS When | Use DFS When |
|--------------|--------------|
| Shortest path (unweighted) | All paths needed |
| Minimum steps/moves | Backtracking required |
| Level-by-level processing | Memory is limited |
| Finding nearest | Detecting cycles |
| Expanding from multiple sources | Topological sort |

### Common Patterns Summary

| Pattern | Use Case |
|---------|----------|
| Standard BFS | Shortest path, minimum steps |
| Multi-source BFS | Distance from multiple starts |
| State-space BFS | Complex states (position + keys, etc.) |
| 0-1 BFS | Weighted graph with only 0/1 weights |
| Bidirectional BFS | Large search space, known start and end |
| BFS + pruning | Optimize by skipping unnecessary states |

### Complexity Notes

| Approach | Time | Space |
|----------|------|-------|
| Standard BFS | O(V + E) | O(V) |
| Grid BFS | O(m × n) | O(m × n) |
| State-space BFS | O(states × transitions) | O(states) |
| Bidirectional BFS | O(√total_states) | O(√total_states) |

### Edge Cases

1. **Start equals target**
2. **No path exists**
3. **Empty graph**
4. **Disconnected components**
5. **Cycles** (must track visited)
6. **Large state space** (consider bidirectional)
7. **Negative conditions** (banned positions, obstacles)

---

Good luck! Start with Part 1-2 for basic BFS and shortest path. Part 4 (state-space BFS) is crucial for harder problems where state is more than just position. Part 5 (0-1 BFS) and Part 7 (bidirectional) are optimization techniques for specific scenarios.
