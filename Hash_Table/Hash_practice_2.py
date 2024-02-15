class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

if __name__ == '__main__':
    ht = Hash_table()
    print(ht.get_hash('march 6'))
    ht['march 6'] = 130
    print(ht.arr)
    print(ht['march 6'])