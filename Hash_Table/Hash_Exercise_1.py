import csv

with open('nyc_weather.csv', mode = 'r') as f:
    mylist = []
    for line in f:
        tokens = line.split(',')
        date = tokens[0]
        temp = tokens[1]
        for char in temp:
            temp = temp[0:2]
        try:
            temp = int(temp)
        except:
            temp = temp
        mylist.append([date, temp])
    mylist = mylist[1:] 
    
    temp = 0
    for i in range(7):
        temp = temp + mylist[i][1]
    temp = temp / 7 


    print(f'Average Temp for a week of Jan is : {temp}')
    max_temp = 0
    newlist = []
    for i in range(len(mylist)):
        newlist.append(mylist[i][1])
    
    print(f'Maximum temperature for the first 10 days of January is :: {max(newlist)}')
 


       
        

   

