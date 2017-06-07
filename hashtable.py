def hash(s):
     hashed = 0
     for i, c in enumerate(s): hashed += 26**(len(s)-i+1) * ord(c)-97
     return hashed


class HashTable(object):
    """
    An open adressing hash table
    >>> hash_table = HashTable(10)
    >>> hash_table.insert("green")
    >>> hash_table.insert("red")
    >>> hash_table.insert("yellow")
    >>> hash_table.insert("blue")
    >>> hash_table.insert("magenta")
    >>> hash_table.insert("cyan")
    >>> hash_table.insert("pink")
    >>> hash_table.insert("gray")
    >>> hash_table.insert("black")
    >>> hash_table.insert("white")
    >>> hash_table.successor("green")
    'magenta'
    >>> hash_table.delete("magenta")
    'magenta'
    >>> hash_table.successor("green")
    'pink'
    >>> hash_table.minimum()
    'black'
    >>> hash_table.maximum()
    'yellow'
    >>> hash_table.delete("black")
    'black'
    >>> hash_table.delete("yellow")
    'yellow'
    >>> hash_table.minimum()
    'blue'
    >>> hash_table.maximum()
    'white'
    """
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.minitem = None
        self.maxitem = None

    def index_for(self, item):
        """
        Gets an index for item bashed on its hash value
        """
        return hash(item) % self.size

    def insert(self, item):
        """
        Inserts an item into the hash table
        """
        if self.minitem is None or self.minitem > item:
            self.minitem = item
        if self.maxitem is None or self.maxitem < item:
            self.maxitem = item
        index = self.index_for(item)
        while self.items[index] != None:
            index += 1 # increment
            index %= self.size # wrap
        self.items[index] = item

    def delete(self, item):
        """
        Deletes an item from the hash table
        """
        index = self.index_for(item)
        count = 0
        while self.items[index] != item and \
              self.items[index] is not None and \
              count != self.size:
            index += 1
            index %= self.size
            count += 1
        if self.items[index] != item:
            return "item not found"
        # delete the item and reorganize
        self.items[index] = None
        temp = [temp_item for temp_item in self.items if temp_item != None]
        self.reset()
        self.minitem = None
        self.maxitem = None
        for temp_item in temp:
            self.insert(temp_item)
        return item

    def reset(self):
        """
        Reinitializes the hashmap
        """
        for i in range(0, self.size):
            self.items[i] = None

    def successor(self, item):
        """
        Finds the successor for an item (or None if it does not exist}
        """
        successor = None
        for consider_item in self.items:
            if consider_item > item:
                if successor is None or consider_item < successor:
                    successor = consider_item
        return successor

    def predecessor(self, item):
        """
        Finds the predecessor for an item (or None if it does not exist)
        """
        predecessor = None
        for consider_item in self.items:
            if consider_item < item:
                if predecessor is None or consider_item > predecessor:
                    predecessor = consider_item
        return predecessor

    def minimum(self):
        """
        Returns the minimum item
        """
        return self.minitem

    def maximum(self):
        """
        Returns the maximum item
        """
        return self.maxitem


if __name__ == "__main__":
    import doctest
    doctest.testmod()
