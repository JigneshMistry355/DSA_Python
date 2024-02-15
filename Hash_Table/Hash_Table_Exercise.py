class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        return self.arr[h]

if __name__ == '__main__':
    ht = HashTable()
    

    ht['A'] = 5
    print(ht.arr, '\n\n\n')
    key = 'A'
    print(f'Value is :: {ht[key]}')
    

