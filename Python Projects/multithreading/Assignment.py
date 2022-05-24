from threading import *
import time


def evennumbers(numbers):
  for i in numbers:
    if i%2==0:
        print(i, ' is  a even number')

def oddnumbers(numbers):
    for i in numbers:
        if i % 2 != 0:
            print(i, ' is  a odd number')


arr = list(range(1,101))

t = time.time() # start monitoring time

t1= Thread(target=oddnumbers, args=(arr,)) # thread using a funciton
t2= Thread(target=evennumbers, args=(arr,)) # Thread using a function

t1.start() # start the thread 1
t2.start() # start the thread 2

t1.join() # wait for thread 1 to complete
t2.join() # wait for thread 2 to complete



print('Done in : ', time.time()-t) # print total time taken
