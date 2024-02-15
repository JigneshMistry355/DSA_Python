class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h %  self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

if __name__ == '__main__':
    ht = Hash_table()
    ht['march 6'] = 130
    ht['march 17'] = 170
    ht['Dec 4'] = 50
    ht['Jan 6'] = 61
    ht['Jan 10'] = 98
    ht['march 6'] = 10
    print(ht.arr)
    print(f'\n Price on March 6 is {ht["march 6"]}')