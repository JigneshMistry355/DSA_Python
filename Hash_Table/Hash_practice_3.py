class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

if __name__ == '__main__':
    ht = Hash_table()

    # print(ht.get_hash('march 9'))
    ht['march 6'] = 130

    

    hash_array = ht.arr
    print(hash_array)


    date = ''
    while True:
        date = input('Enter date : ')
        
        if date == 'q':
            print("Are you sure you want to exite ")
            confirm_exit = input('Press y/n \n')
            if confirm_exit == 'y':
                break

              

        print(f'Value on {date} is {ht[date]}')