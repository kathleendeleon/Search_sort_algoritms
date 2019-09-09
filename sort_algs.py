#Sorting Algorithms

from random import randint,shuffle

def create_array(length=10,maxint=50):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr


def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swapped=True
    return arr
        
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    smaller,equal,larger=[],[],[]
    pivot=arr[randint(0,len(arr)-1)]
    for i in arr:
        if i<pivot:
            smaller.append(i)
        elif i==pivot:
            equal.append(i)
        else:
            larger.append(i)
    return(quick_sort(smaller)+equal+quick_sort(larger))

def mergesort(a,b):
    c=[]
    a_idx,b_idx=0,0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1
    if a_idx==len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c

def merge_sort(a):
    if len(a)<=1:
        return a
    left,right=merge_sort(a[:len(a)//2]),merge_sort(a[len(a)//2:])
    return mergesort(left,right)   

#def bogo_sort(arr):

#def insert_sort(arr);

#def selection_sort(arr):
    
    
    
    

def benchmark(n=[10,100,1000]):
    from time import time
    builtin=[]
    bubble=[]
    quick=[]
    merge=[]
    for length in n:
        a=create_array(length,length)
        
        t0=time()
        s=sorted(a)
        t1=time()
        builtin.append(t1-t0)

        t0=time()
        s=bubbleSort(a)
        t1=time()
        bubble.append(t1-t0)

        t0=time()
        s=quick_sort(a)
        t1=time()
        quick.append(t1-t0)

        t0=time()
        s=merge_sort(a)
        t1=time()
        merge.append(t1-t0)

    print("n \tBuil-in \tBubble Sort \tQuick Sort \tMerge Sort")
    print("_________________________________________________________________")
    for i,cur_n in enumerate(n):
        print("%d\t%f \t%f \t%f \t%f"%(cur_n,builtin[i],bubble[i],quick[i],merge[i]))
        





