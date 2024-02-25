import math


def calc_shortest_path(g, start, goal):
    undetermined = dict(g)  # 最短経路が未確定のノード（ノードをキー、隣接ノードとの関係を表したdict型を値とするdict型）
    node_distances = dict()  # ノードをキー、始点からの距離を値とするdict型
    pre_nodes = dict()  # ノードをキー、1つ手前のノードを値とするdict型

    # 初期値として無限大を設定する
    for nodes in undetermined:
        node_distances[nodes] = math.inf
    # 開始地点に0を設定
    node_distances[start] = 0

    # 全てのノードが確定するまで処理を行う
    while undetermined:

        # 最短距離のダンプ
        print(node_distances)

        # 未確定ノードの中で始点からの距離が最小のものを探し、これを確定済みとする
        minimum_node = None
        for node in undetermined:
            if minimum_node is None:
                minimum_node = node
            elif node_distances[node] < node_distances[minimum_node]:
                minimum_node = node

        # 確定したノードから直接繋がっている未確定ノードに対し始点からの距離を更新する
        for node, distance in undetermined[minimum_node].items():
            if distance + node_distances[minimum_node] < node_distances[node]:
                # 始点からの距離を更新
                node_distances[node] = distance + node_distances[minimum_node]
                # 始点からそのノードに最短経路でたどる場合の直前のノードを格納
                pre_nodes[node] = minimum_node

        # minimum_nodeが確定したので未確定の中から削除する
        undetermined.pop(minimum_node)

    # pre_nodesに基づき目的地から逆に最短経路を構築
    node = goal
    shortest_path = []
    while node != start:
        shortest_path.insert(0, node)
        node = pre_nodes[node]

    shortest_path.insert(0, start)

    if node_distances[goal] != math.inf:
        print('最短経路：', shortest_path)
        print('最短距離：', node_distances[goal])


graph = {
    "A": {"B": 1, "C": 3, "D": 3},
    "B": {"A": 1, "C": 1},
    "C": {"A": 3, "B": 1, "E": 4, "F": 5},
    "D": {"A": 3, "D": 4},
    "E": {"C": 4, "D": 4, "G": 2, "H": 4},
    "F": {"C": 5, "H": 3},
    "G": {"E": 2, "H": 1},
    "H": {"E": 4, "F": 3, "G": 1},
}

calc_shortest_path(graph, "A", "H")
