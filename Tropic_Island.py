from heapq import heappush as hpush, heappop as hpop


def rainfall(island, N, M):
    queue = []
    visited = set()
    collected = 0
    for i in ((x, y) for x in (0, N - 1) for y in range(1, M - 1)): hpush(queue, (island[i[0]][i[1]], i))
    for i in ((x, y) for x in range(1, N - 1) for y in (0, M - 1)): hpush(queue, (island[i[0]][i[1]], i))
    while queue:
        lh, v = queue[0]
        while queue:
            h, v = hpop(queue)
            if v not in visited:
                if h > lh:
                    hpush(queue, (h, v))
                    break
                visited.add(v)
                collected += lh - h
                for dxy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                    x, y = v[0] + dxy[0], v[1] + dxy[1]
                    if N - 1 > x > 0 and M - 1 > y > 0:
                        hpush(queue, (island[x][y], (x, y)))
    return collected

if __name__ == '__main__':
    world_size = int(input())
    while world_size:
        s = input().split()
        N, M = int(s[0]), int(s[1])
        island = [[int(j) for j in input().split()] for i in range(N)]
        print(rainfall(island, N, M))
        world_size -= 1

    '''import sys
    data = sys.stdin.read()
    world = [i.split() for i in data[:-1].split('\n')]
    world_size, dv = int(world[0][0]), 1
    while world_size != 0:
        island = []
        N, M = int(world[dv][0]), int(world[dv][1])
        for x in range(dv+1, dv+N+1):
            isl = []
            for y in range(M):
                isl.append(int(world[x][y]))
            island.append(isl)
        sys.stdout.write(str(rainfall(island, N, M)) + '\n')
        world_size -= 1
        dv += N+1'''

