class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        Видаляє пару ключ-значення з хеш-таблиці.
        Повертає True, якщо видалення успішне, і False, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        
        if self.table[key_hash] is None:
            return False
        
        # Проходимо по списку (ланцюжку) в слоті
        for i in range(len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
                
        return False

# --- Тестування ---
if __name__ == "__main__":
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(f"Початкове значення 'apple': {H.get('apple')}")
    
    # Видалення існуючого ключа
    result = H.delete("apple")
    print(f"Видалення 'apple': {result}")
    print(f"Значення 'apple' після видалення: {H.get('apple')}")
    
    # Спроба видалення неіснуючого ключа
    print(f"Видалення 'cherry': {H.delete('cherry')}")
