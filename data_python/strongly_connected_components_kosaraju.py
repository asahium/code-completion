class Kosaraju:
    def dfs(self, i, V, adj, visited, stk):
        visited[i] = 1

        for x in adj[i]:
            if visited[x] == -1:
                self.dfs(x, V, adj, visited, stk)

        stk.append(i)

    def kosaraju(self, V, adj):

        stk, visited = [], [-1]*(V+1)

        for i in range(V):
            if visited[i] == -1:
                self.dfs(i, V, adj, visited, stk)

        stk.reverse()
        res = stk.copy()

        ans, visited1 = 0, [-1]*(V+1)

        adj1 = [[] for x in range(V)]

        for i in range(len(adj)):
            for x in adj[i]:
                adj1[x].append(i)

        for i in range(len(res)):
            if visited1[res[i]] == -1:
                ans += 1
                self.dfs(res[i], V, adj1, visited1, stk)

        return ans


def main():
    V, E = map(int, input().split())
    adj = [[] for x in range(V)]

    for i in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)

    print(Kosaraju().kosaraju(V, adj))


if __name__ == '__main__':
    main()
