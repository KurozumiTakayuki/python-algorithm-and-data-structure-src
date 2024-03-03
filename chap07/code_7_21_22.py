from string import ascii_letters


def my_hash_func(text):
    hash_num = 0
    for c in text:
        hash_num += ascii_letters.index(c)
    return hash_num


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.value) + " - " + str(self.next)
        else:
            return str(self.value)


class MyHashTable:

    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def set(self, key, value):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]

        # データがない場合はそこに設定
        if not node:
            self.data[hash_key] = Node(key, value)
            return

        # 終端まで辿る
        while node.next:
            node = node.next

        # 終端のnextに設定
        node.next = Node(key, value)

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]
        if node is None:
            print("データが見つかりませんでした")
            return

        # キーが一致するまで辿る
        while node.key != key:
            node = node.next
            if node is None:
                print("データが見つかりませんでした")
                return

        return node.value

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        node = self.data[hash_key]
        if node is None:
            print("データが見つかりませんでした")
            return

        # 1つ手前のノードを保持する
        pre_node = None

        # キーが一致するまで辿る
        while node.key != key:
            pre_node = node
            node = node.next
            if node is None:
                print("データが見つかりませんでした")
                return

        # 1つ手前のノードと次のノードを連結する
        pre_node.next = node.next

    def __str__(self):
        result = ""
        for idx, node in enumerate(self.data):
            if node:
                result += str(idx) + ":" + str(node) + "\n"
        return result


my_map = MyHashTable()
my_map.set("suzuki", "suzuki@example.com")
my_map.set("nakata", "nakata@example.com")
my_map.set("tanaka", "tanaka@example.com")
my_map.set("kanata", "kanata@example.com")

print(my_map)
my_map.delete("tanaka")
print(my_map)
print(my_map.get("kanata"))
