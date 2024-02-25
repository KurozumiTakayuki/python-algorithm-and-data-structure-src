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

    def __str__(self):
        return "{key}:{value}".format(key=self.key, value=self.value)


class MyHashTable:

    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def set(self, key, value):
        hash_key = my_hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None or node.key == '-':
                self.data[hash_key] = Node(key, value)
                return

            # ハッシュ値の再計算
            hash_key += 1

        print("空きが見つかりませんでした")

    def get(self, key):
        hash_key = my_hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("データが見つかりませんでした")
                return

            elif node.key == key:
                return node.value

            # ハッシュ値の再計算
            hash_key += 1

        print("データが見つかりませんでした")

    def delete(self, key):
        hash_key = my_hash_func(key) % self.size
        while hash_key < self.size:
            node = self.data[hash_key]
            if node is None:
                print("データが見つかりませんでした")
                return

            elif node.key == key:
                self.data[hash_key] = Node('-', None)
                return

            # ハッシュ値の再計算
            hash_key += 1

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

print(my_map)
my_map.delete("nakata")
print(my_map)
val = my_map.get("tanaka")
print(val)
my_map.set("kanata", "kanata@example.com")
print(my_map)
