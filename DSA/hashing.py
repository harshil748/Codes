def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size, method="chaining"):
        self.size = next_prime(size)
        self.table = [None] * self.size
        self.method = method

    def hash_function(self, key):
        return key % self.size

    def insert_item(self, key, value):
        index = self.hash_function(key)

        if self.method == "chaining":
            new_node = Node(key, value)
            if self.table[index] is None:
                self.table[index] = new_node
            else:
                current = self.table[index]
                while current.next:
                    current = current.next
                current.next = new_node

        elif self.method == "linear_probing":
            original_index = index
            while self.table[index] is not None and self.table[index][0] != key:
                index = (index + 1) % self.size
                if index == original_index:
                    raise Exception("Hash table is full!")
            self.table[index] = (key, value)

    def delete_item(self, key):
        index = self.hash_function(key)

        if self.method == "chaining":
            current = self.table[index]
            prev = None
            while current:
                if current.key == key:
                    if prev:
                        prev.next = current.next
                    else:
                        self.table[index] = current.next
                    return
                prev = current
                current = current.next

        elif self.method == "linear_probing":
            original_index = index
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    self.table[index] = None
                    return
                index = (index + 1) % self.size
                if index == original_index:
                    break

    def display_hash(self):
        if self.method == "chaining":
            for i in range(self.size):
                print(f"table[{i}]", end=" --> ")
                current = self.table[i]
                while current:
                    print(f"({current.key}, {current.value})", end=" --> ")
                    current = current.next
                print("None")
        elif self.method == "linear_probing":
            for i in range(self.size):
                if self.table[i] is None:
                    print(f"table[{i}] --> None")
                else:
                    print(f"table[{i}] --> ({self.table[i][0]}, {self.table[i][1]})")



print("Using Separate Chaining:")
hash_table = HashTable(6, method="chaining")
hash_table.insert_item(231, 123)
hash_table.insert_item(326, 432)
hash_table.insert_item(212, 523)
hash_table.insert_item(321, 43)
hash_table.insert_item(433, 423)
hash_table.insert_item(262, 111)
hash_table.display_hash()
print("\nAfter deleting record with student ID 212:")
hash_table.delete_item(212)
hash_table.display_hash()

print("\nUsing Linear Probing:")
hash_table_lp = HashTable(6, method="linear_probing")
hash_table_lp.insert_item(231, 123)
hash_table_lp.insert_item(326, 432)
hash_table_lp.insert_item(212, 523)
hash_table_lp.insert_item(321, 43)
hash_table_lp.insert_item(433, 423)
hash_table_lp.insert_item(262, 111)
hash_table_lp.display_hash()
print("\nAfter deleting record with student ID 212:")
hash_table_lp.delete_item(212)
hash_table_lp.display_hash()
