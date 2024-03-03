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


left_node = Node('C', 1)
right_node = Node('E', 1)
parent_node = Node('CE', 2)
parent_node.left = left_node
parent_node.right = right_node
parent_node.left.code = "0"
parent_node.right.code = "1"
result_dict = dict()
build_code_dict(parent_node, "", result_dict)
print(result_dict)
