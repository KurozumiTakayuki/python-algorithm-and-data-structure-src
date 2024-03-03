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


node1 = Node("key1", "data1")
node2 = Node("key2", "data2")
node3 = Node("key3", "data3")
node1.next = node2
node2.next = node3
print(node1)
