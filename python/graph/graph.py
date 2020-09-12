from collections import deque


class Graph:
    """
    无向图,采用邻接表存储
    v 顶点个数
    adj 边
    visited 被访问过的定点
    d 队列
    pre 搜索路径
    """

    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def bfs(self, s, t):
        if s == t:
            return
        visited = [False for _ in range(self.v)]
        visited[s] = True
        d = deque()
        d.append(s)
        prev = [-1 for _ in range(self.v)]
        while d:
            k = d.popleft()
            for i in self.adj[k]:
                if visited[i]:
                    continue
                prev[i] = k
                if i == t:
                    self.print_path(prev, s, t)
                    return
                visited[i] = True
                d.append(i)

    def print_path(self, prev, s, t):
        if t != s:
            self.print_path(prev, s, prev[t])
        print(t)


if __name__ == '__main__':
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(3, 4)
    g.add_edge(0, 3)
    g.add_edge(3, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 4)

    g.bfs(1, 4)
