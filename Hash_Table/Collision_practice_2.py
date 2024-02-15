class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key, value)
                found = True
                return
        if not(found):
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]    

if __name__ == '__main__':
    ht = Hash_table()

    ht['march 6'] = 130
    ht['march 17'] = 400


    hash_array = ht.arr
    print(hash_array)

    print(f'Value on march 6 is {ht["march 6"]}')
    