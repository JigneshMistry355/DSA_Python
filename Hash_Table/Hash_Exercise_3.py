class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        count = 0
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                count = element[1]
                count += 1
                self.arr[h][i] = [key, count]
                found = True
                break
        if not found:
            count += 1
            self.arr[h].append([key, count])
            

        return count
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

if __name__ == '__main__':
    ht = Hash_table()
    with open('poem.txt', "r") as f:
        mylist = []
        for para in f:
            lines = para.split(',')
            for line in lines:
                word = line.split(" ")
                mylist.append(word)
        # print(mylist)


        wordList = []
        for i in range(len(mylist)):
            for j in range(len(mylist[i])):
                wordList.append(mylist[i][j])
        # print(wordList,"\n\n")
                
        for i in range(len(wordList)):
            ht[wordList[i]] = wordList[i]

        # print(ht.arr)

        # print(f'\n\n{ht["And"]}')

        # while True:
        #     word = input("")
        #     if word == 'Exit':
        #         break
            # print(f"\'{word}\' : {ht[word]}")

        # print(wordList[10: 21])
            
        # cleaning data
        print(wordList)
        for i in range(len(wordList)):
            for char in range(len(wordList[i])):
                
                print(wordList[i][char], char)
                print(ord(wordList[i][char]))
                if (ord(wordList[i][char]) in range(65,91)) or (ord(wordList[i][char]) in range(97,123)):
                    print("in range")
                    wordList[i][char] = None
            break
                    
                
        # break
        print(wordList)
                # print(wordList[i])
                # # print(ord(wordList[1][2]))
                # if not (ord(wordList[i][char]) in range(65,91)) or (ord(wordList[i][char]) in range(97,123)):
                #     wordList[i] = wordList[i][:]
                #     break
            
        # print(wordList)


