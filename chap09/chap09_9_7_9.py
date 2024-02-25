from bst_dump import dump


class Node:
    def __init__(self, key, value, is_left=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.is_left = is_left

    def __str__(self):
        return str(self.key) + ":" + str(self.value)


class MyBsTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        # rootがない場合はrootに設定
        if self.root is None:
            self.root = Node(key, value)
            return

        self._add_node(self.root, key, value)

    def _add_node(self, node, key, value):
        if key == node.key:
            print("指定したキーは既に存在するため追加できませんでした", key)
            return

        if key < node.key:
            # 指定したキーが現在のノードのキーより小さい場合
            if not node.left:
                # 左側に空きがあればそこに設定
                node.left = Node(key, value, is_left=True)
                return
            else:
                # 左側に空きがなければ左側を再帰的に辿る
                self._add_node(node.left, key, value)
        else:
            # 指定したキーが現在のノードのキーより大きい場合
            if not node.right:
                # 右側に空きがあればそこに設定
                node.right = Node(key, value, is_left=False)
                return
            else:
                # 右側に空きがなければ右側を再帰的に辿る
                self._add_node(node.right, key, value)

    def get(self, key):
        return self._get_node(self.root, key)

    def _get_node(self, node, key):
        if node is None:
            print("指定したキーのノードは見つかりませんでした")
            return node

        if key == node.key:
            # 引数で指定したキーとノードのキーが一致
            return node

        # ルートから指定したキーのノードまで再帰的に辿る
        if key < node.key:
            # 指定したキーが現在のノードのキーより小さい場合、左側を再帰的に辿る
            return self._get_node(node.left, key)
        else:
            # 指定したキーが現在のノードのキーより大きい場合、右側を再帰的に辿る
            return self._get_node(node.right, key)

    def delete(self, key):
        node = self.root
        self._del_node(node, key)

    def _del_node(self, node, key):
        if node is None:
            print("指定したキーのノードは見つかりませんでした")
            return node

        # ルートから指定したキーのノードまで再帰的に辿る
        if key < node.key:
            # キーがノードより小さい場合、左部分木でノードを探索
            node.left = self._del_node(node.left, key)
            if node.left:
                node.left.is_left = True
            return node
        if key > node.key:
            # キーがノードより大きい場合、右部分木でノードを検索
            node.right = self._del_node(node.right, key)
            if node.right:
                node.right.is_left = False
            return node

        # 子がない若しくは左右一方のみに子がある場合、後継ノードとしてその子を返す
        if node.right is None:
            if node == self.root:
                # 対象ノードがルートの場合は自身を子に付け替え
                self.root = node.left
            return node.left
        if node.left is None:
            if node == self.root:
                # 対象ノードがルートの場合は自身を子に付け替え
                self.root = node.right
            return node.right

        # 両側に子がある場合、左部分木の最大ノードを後継ノードとする
        successor = node.left
        while successor.right:
            successor = successor.right

        # 後継ノードの情報をコピー
        node.key = successor.key
        node.value = successor.value

        # 削除対象ノードの左部分木から後継ノードを削除する
        node.left = self._del_node(node.left, successor.key)
        if node.left:
            node.left.is_left = True
        return node


def main():
    bst = MyBsTree()
    bst.add(8, "Suzuki")
    bst.add(3, "Tanaka")
    bst.add(9, "Takahashi")
    bst.add(2, "Yamashita")
    bst.add(6, "Sato")
    bst.add(1, "Ito")
    bst.add(5, "Watanabe")
    dump(bst)
    bst.delete(8)
    dump(bst)


main()
