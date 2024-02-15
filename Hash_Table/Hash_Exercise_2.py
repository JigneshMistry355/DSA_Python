class Hast_table:
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
    ht = Hast_table()
    with open('Hash_Table/nyc_weather.csv') as f:
        mylist = []
        for line in f:
            token = line.split(',')
            date = token[0]
            temp = token[1]
            for char in temp:
                temp = temp[0:2]
            try:
                temp = int(temp)
            except:
                temp = temp
            mylist.append([date, temp])
        mylist = mylist[1:]

    for i in range(len(mylist)):
        ht[mylist[i][0]] = mylist[i][1]
    
    print(f'The temperature on Jan 9 is {ht["Jan 9"]}')
    print(f'The temperature on Jan 4 is {ht["Jan 4"]}')

    