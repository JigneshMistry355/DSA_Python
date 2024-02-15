import threading
import time



def square(mylist):
    for i in mylist:
        time.sleep(0.5)
        print('square : ',i*i)

def cube(mylist):
    for i in mylist:
        time.sleep(0.5)
        print('cube : ',i*i*i)
    # return list(map(lambda x: x*x*x, mylist))
    

if __name__ == '__main__':
    mylist = [2,3,4,5]

    t = time.time()

    t1 = threading.Thread(target=square, args=(mylist,))
    t2 = threading.Thread(target=cube, args=(mylist,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done in ',time.time() -t)
  