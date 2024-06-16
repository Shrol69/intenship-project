class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def display(self):
        print("Hash Table with Separate Chaining:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")
        print()


class HashTableProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def display(self):
        print("Hash Table with Linear Probing:")
        for i, pair in enumerate(self.table):
            if pair:
                print(f"Slot {i}: {pair}")
            else:
                print(f"Slot {i}: Empty")
        print()


if __name__ == "__main__":
    print("Select Hash Table Collision Resolution Strategy:")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        hash_table = HashTableChaining(10)
    elif choice == '2':
        hash_table = HashTableProbing(10)
    else:
        print("Invalid choice. Exiting.")
        exit()

    while True:
        print("\nOptions:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Exit")
        option = input("Choose an option: ")

        if option == '1':
            key = input("Enter key to insert: ")
            value = input("Enter value to insert: ")
            hash_table.insert(key, value)
        elif option == '2':
            key = input("Enter key to delete: ")
            if hash_table.delete(key):
                print("Key deleted successfully.")
            else:
                print("Key not found.")
        elif option == '3':
            key = input("Enter key to search: ")
            result = hash_table.search(key)
            if result is not None:
                print(f"Value for key '{key}': {result}")
            else:
                print("Key not found.")
        elif option == '4':
            hash_table.display()
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
