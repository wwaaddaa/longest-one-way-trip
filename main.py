import sys

sys.setrecursionlimit(100000)

graph = {}
total_edge = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    data = line.split(",")
    if len(data) < 3:
        continue
    a = int(data[0])
    b = int(data[1])
    d = float(data[2])
    graph.setdefault(a, []).append((b, d))
    graph.setdefault(b, []).append((a, d))
    total_edge += d

# 各駅に接する辺の最大値(枝刈り用の緩い上界の計算に使用)
max_distance = -1.0
best_route = []


def dfs(start, current, visited, route, distance, remaining):
    global max_distance, best_route

    if distance > max_distance:
        max_distance = distance
        best_route = route.copy()

    # 残りの辺をすべて使っても更新できないなら打ち切る
    if distance + remaining <= max_distance:
        return

    for nxt, d in graph[current]:
        if nxt == start and len(route) >= 3:
            if distance + d > max_distance:
                max_distance = distance + d
                best_route = route + [start]
        elif nxt not in visited:
            visited.add(nxt)
            route.append(nxt)
            dfs(start, nxt, visited, route, distance + d, remaining - d)
            route.pop()
            visited.remove(nxt)


for start in graph:
    dfs(start, start, {start}, [start], 0.0, total_edge)

sys.stdout.reconfigure(newline="")
sys.stdout.write("".join(f"{s}\r\n" for s in best_route))