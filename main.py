
import sys

# 駅と駅のつながりを保存する
graph = {}

# 標準入力からデータを読み込む
for line in sys.stdin:
    if not line.strip():
        continue

    data = line.strip().split(",")

    station_a = int(data[0])
    station_b = int(data[1])
    distance = float(data[2])

    if station_a not in graph:
        graph[station_a] = []

    if station_b not in graph:
        graph[station_b] = []

    # 双方向のつながりを登録する
    graph[station_a].append((station_b, distance))
    graph[station_b].append((station_a, distance))


# 最長ルートを保存する
max_distance = -1
best_route = []


# 最長ルートを更新する関数
def update_best(distance, route):
    global max_distance, best_route

    if distance > max_distance:
        max_distance = distance
        best_route = route.copy()


# 深さ優先探索
def dfs(start, current, visited, route, distance):

    # 現在までのルートも候補として記録する
    update_best(distance, route)

    # 現在の駅から行ける駅を調べる
    for next_station, next_distance in graph[current]:

        # 始点に戻る場合は、ルートを閉じる
        if next_station == start and len(route) >= 3:
            update_best(
                distance + next_distance,
                route + [start]
            )

        # 訪問していない駅なら進む
        elif next_station not in visited:

            visited.add(next_station)
            route.append(next_station)

            dfs(
                start,
                next_station,
                visited,
                route,
                distance + next_distance
            )

            # 元の状態に戻る
            route.pop()
            visited.remove(next_station)


# すべての駅から探索する
for start in graph:

    visited = {start}
    route = [start]

    dfs(start, start, visited, route, 0)


# 駅IDだけを1行ずつ出力する
for station in best_route:
    print(station)
