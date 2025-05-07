from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()  # Track all vertices explicitly

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if not visited.get(i, False):
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = {vertex: False for vertex in self.vertices}
        if start not in visited:
            print("Start vertex not found in graph.")
            return
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = {vertex: False for vertex in self.vertices}
        if start not in visited:
            print("Start vertex not found in graph.")
            return
        queue = [start]
        visited[start] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

def main():
    g = Graph()

    while True:
        print("\n1. Add Edge")
        print("2. Depth First Search (DFS)")
        print("3. Breadth First Search (BFS)")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            u = int(input("Enter source vertex: "))
            v = int(input("Enter destination vertex: "))
            g.add_edge(u, v)
        elif choice == '2':
            start = int(input("Enter starting vertex for DFS: "))
            print("DFS traversal:")
            g.dfs(start)
        elif choice == '3':
            start = int(input("Enter starting vertex for BFS: "))
            print("BFS traversal:")
            g.bfs(start)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
