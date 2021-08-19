from collections import deque

def read_tree():
    n = int(input())
    
    tree = []
    for _ in range(n):
        tree.append([])

    for _ in range(1, n):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1

        tree[u].append(v)
        tree[v].append(u)

    return tree 


def bfs_tree(tree, start=0):
    q = deque()
    q.append((start, -1))

    timer = [0] * len(tree)
    while len(q) > 0:
        u, p = q.popleft()

        if p != -1:
            timer[u] = timer[p] + 1

        for v in tree[u]:
            if v != p:
                q.append((v, u))

    mv = max(timer)
    return (mv, timer.index(mv))


def max_tree_path(tree):
    _, v = bfs_tree(tree)
    r, _ = bfs_tree(tree, v)

    return r


if __name__ == '__main__':
    ta = read_tree()
    tb = read_tree()

    a = max_tree_path(ta)
    b = max_tree_path(tb)

    if (a + 1) // 2 > b:
        print('L')
    else:
        print('D')
