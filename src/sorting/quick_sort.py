from random import choice, shuffle
from time import time

def quick_sort(ar):
    
    
    pivot = choice(ar)
    ar.remove(pivot)
    left = [elem for elem in ar if elem <= pivot]
    right = [elem for elem in ar if elem > pivot]
    
    if len(left) > 1: 
        left = quick_sort(left)
    if len(right) > 1: 
        right = quick_sort(right)
    
    return left + [pivot] + right

if __name__ == "__main__":
    time_list1, time_list2 = [], []
    for i in xrange(100):
        a = range(50000)
        shuffle(a)
        b = a[:]
        init_time = time()
        quick_sort(a)
        time_list1.append(time()-init_time)
        
        init_time = time()
        b.sort()
        time_list2.append(time()-init_time)
    print sum(time_list1), sum(time_list2)
        
        
      

