class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
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
            
    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i] 
                break



if __name__ == '__main__':
    ht = Hash_Table()
    ht['march 6'] = 10
    ht['march 17'] = 12
    ht['march 8'] = 12
    ht['march 9'] = 12
    print(ht['march 17'])
    # del ht['march 17']
    print(ht.arr)