class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        # シンボル
        self.symbol = symbol

        # 頻度
        self.freq = freq

        # 左子
        self.left = left

        # 右子
        self.right = right

        # 符号 (0 or 1)
        self.code = ''

    def __lt__(self, other):
        # 比較演算の定義
        return self.freq < other.freq

    def __str__(self):
        return self.symbol


def aggregate_frequency(text):
    freq: dict = dict()
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    return sorted(freq.items(), key=lambda item: item[1], reverse=True)


def build_code_dict(node, parent_code, result_dict):
    """
    頂点ノードから再帰的にハフマン符号化の符号辞書を構築する
    """
    current_code = parent_code + node.code

    # 左右いずれかに子がある場合、再帰的に処理を行う
    if node.left:
        build_code_dict(node.left, current_code, result_dict)
    if node.right:
        build_code_dict(node.right, current_code, result_dict)

    # 子がない場合はリーフノードなので結果をresult_dictに格納する
    if not (node.left or node.right):
        result_dict[node.symbol] = current_code


def build_huffman_tree(text):
    # 頻度のリスト
    freq_list = aggregate_frequency(text)

    # ノード格納用のリスト
    nodes = []

    # ノードリストを構築
    for symbol, freq in freq_list:
        node = Node(symbol, freq)
        nodes.append(node)

    # ループ処理でハフマンツリーを構築（要素数が2以上の間ループを継続する）
    while 2 <= len(nodes):
        # 降順にソート
        nodes = sorted(nodes, reverse=True)

        # 要素を末端から2つ取り出す
        right = nodes.pop(-1)
        left = nodes.pop(-1)

        # それぞれのノードに符号を割り当て（左=0、右=1）
        left.code = "0"
        right.code = "1"

        # 親ノードparentを生成
        # 子のシンボルを結合したものを親のシンボルとする
        parent_symbol = left.symbol + right.symbol
        # 子の頻度を合算したものを親の頻度とする
        parent_freq = left.freq + right.freq
        parent = Node(parent_symbol, parent_freq, left, right)

        # ノードリストの末尾にparentを追加する
        nodes.append(parent)

    # ここで符号化が完了
    root = nodes[0]

    # 以下、符号化結果を表示
    result_dict = dict()
    build_code_dict(root, "", result_dict)
    print(result_dict)


build_huffman_tree("BDDAAAABACEBBBAA")
