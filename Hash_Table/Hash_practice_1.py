class Hash_table:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    

if __name__ == '__main__':
    ht = Hash_table()
    ht['march 6'] = 130
    # print(ht.get_hash(key))
    print(ht['march 6'])
    print(ht.arr)