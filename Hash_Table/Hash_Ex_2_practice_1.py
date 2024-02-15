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
   
    with open('Hash_Table/nyc_weather.csv', 'r') as f:
        temp_list = []
        for line in f:
            token = line.split(',')
            date = token[0]
            temp = token[1]
            for char in temp:
                try:
                    temp = temp[:2]
                    temp = int(temp)
                except:
                    temp = temp
            temp_list.append([date, temp])
        print(temp_list)
        for date, temp in temp_list:
            ht[date] = temp

        result = ht.arr
        print(result)

        Jan9 = ht['Jan 9']
        print(f'Temperature on 9th Jan is {Jan9}')