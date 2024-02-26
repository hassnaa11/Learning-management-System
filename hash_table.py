class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.key)


class HashTable_iterator:
    def __init__(self, index):
        self.curr = ht.table[index]

    def __next__(self):
        curr = self.curr.next
        if curr is None:
            raise StopIteration()
        self.curr = curr
        return curr


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def iter(self, key):
        index = self.__hash(key)
        return HashTable_iterator(self, index)

    def __repr__(self):
        data_str = ""
        for i in range(len(self.table)):
            current = self.table[i]
            if current != None:
                data_str = data_str + " " + str(current.key)
                if current.next:
                    data_str = data_str + " " + str(current.next.key)
        return data_str

    def __hash(self, key):
        return hash(key) % self.capacity

    # def get_index(self,key):
    #     return hash(key) * self.capacity

    def insert(self, key, value):
        index = self.__hash(key)
        print("index:", index)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            print("kk")
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self.__hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        index = self.__hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def get_len(self, key):
        length = 1
        index = self.__hash(key)
        current = self.table[index]
        print("curr: ", current)
        while current.next:
            length += 1
            current = current.next
            print("curr: ", current)

        return length


# Driver code
# if __name__ == "_main_":

# Create a hash table with
# a capacity of 5
ht = HashTable(5)

# # Add some key-value pairs
# # to the hash table
ht.insert("DS", "Ahmed")
ht.insert("DS", "Hasnaa")
ht.insert("db", "shahd")
ht.insert("electronics", "mohamed")
print("hash:", ht)
# n = ht.table[3]
# print("itr:", n)
# print("len:", ht.get_len("db"))
print("Node:", ht.search("DS"))
# for ind in ht.table[3]:
#     print("Nodeee:", ind)

# Check if the hash table
# contains a key
# print("apple" in ht)  # True
# print("durian" in ht)  # False

# # Get the value for a key
# print(ht.search("banana"))  # 2

# # Update the value for a key
# ht.insert("banana", 4)
# print(ht.search("banana"))  # 4

# ht.remove("apple")
# # Check the size of the hash table
# print(len(ht))  # 3
