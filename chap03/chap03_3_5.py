class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self, head_value):
        self.head = Node(head_value)

    def append(self, value):
        # 新たにノード生成
        new_node = Node(value)

        # 先頭から順にリンクが設定されていないノード(=終端ノード)まで辿る
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        # 終端ノードのnextに生成したnodeを設定する
        current_node.next = new_node

    def __str__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node))
            current_node = current_node.next

        return "-".join(nodes)


my_list = SinglyLinkedList(35)
my_list.append(22)
my_list.append(8)
print(my_list)
my_list.append(15)
print(my_list)
