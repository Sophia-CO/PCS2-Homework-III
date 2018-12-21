import heapq
import time
import random
import matplotlib.pyplot as plt

#QUICKSORT
def partition(arr,low,high):
    i = (low -1) #smaller index numbers
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1 , high)

def measure_this(size):
    mylist = []
    for i in range(size):
        mylist.append(random.randint(0,size))

#BINARY TREE
class BinaryTree(object):
    def __init__(self):
        self.content = []

    def add(self,value):
        self.content.append(value)
        self.content.sort()

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]

#BinaryHeapTree
class MinMaxBinaryHeap(object):
    def __init__(self):
        self.content=[]

    def add(self,value):
        self.content.append(value)

    def get_min(self):
        return min(self.content)

    def get_max(self):
        return max(self.content)

class BinHeap:
    def __init__(self):
        self.heaplist = [20,23,34,67] #you can insert any number here
        self.currentSize = 0

    def Parents(self,i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist [i//2]:
                pass
            elif self.heaplist[i] > self.heaplist [i//2]:
                j = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist [i]
                self.heaplist[i] = j
            i = i//2

    def insert(self, value):
        self.heaplist.append(value)
        self.currentSize = self.currentSize + 1
        self.Parents(self.currentSize)




#BINARYHEAP
class MinMaxHeap(object):
    def __init__(self):
        self.content_min = []
        self.content_max = []
        # heapq.heapify(self.content_min)
        # heapq.heapify(self.content_max)

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]

    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]

#BUBBLESORT
class MinMaxBubble(object):

    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp

    def add(self, value):
        self.content.append(value)
        self.bubble_sort()

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        add = a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)
    return tot_time_add, tot_time_min, tot_time_max

print (measure_time)

if __name__ == '__main__':
    a = BinaryTree()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())

    a = MinMaxBinaryHeap()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())

    a = MinMaxHeap()
    a.add(5)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(7)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(3)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(9)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())

    a = MinMaxBubble()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())

repetitions = 5
max_operations = 1000
step = 200

values_heap_add, values_heap_min, values_heap_max = [], [], []
values_binaryheap_add, values_binaryheap_min, values_binaryheap_max = [], [], []
values_bubble_add, values_bubble_min, values_bubble_max = [], [], []
values_tree_add, values_tree_min, values_tree_max = [], [], []

for rounds in range(step, max_operations, step):
    this_list = []
    for r in range(rounds):
        this_list.append(random.randint(0, 1000))

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(repetitions):
        a = BinaryTree()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= repetitions
    tot_time_min /= repetitions
    tot_time_max /= repetitions

    values_tree_add.append(tot_time_add * 1000)
    values_tree_min.append(tot_time_min * 1000)
    values_tree_max.append(tot_time_max * 1000)

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(repetitions):
        a = MinMaxBinaryHeap()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= repetitions
    tot_time_min /= repetitions
    tot_time_max /= repetitions

    values_binaryheap_add.append(tot_time_add * 1000)
    values_binaryheap_min.append(tot_time_min * 1000)
    values_binaryheap_max.append(tot_time_max * 1000)

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(5):
        a = MinMaxHeap()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= 5
    tot_time_min /= 5
    tot_time_max /= 5

    values_heap_add.append(tot_time_add * 1000)
    values_heap_min.append(tot_time_min * 1000)
    values_heap_max.append(tot_time_max * 1000)

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(repetitions):
        a = MinMaxBubble()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= repetitions
    tot_time_min /= repetitions
    tot_time_max /= repetitions

    values_bubble_add.append(tot_time_add * 1000)
    values_bubble_min.append(tot_time_min * 1000)
    values_bubble_max.append(tot_time_max * 1000)


#GRAPH
xlabels = range(step, max_operations, step)
plt.plot(xlabels, values_tree_add, label='Add')
plt.plot(xlabels, values_tree_min, label='Get Min')
plt.plot(xlabels, values_tree_max, label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Execution time (msec)")
plt.title("Performance of Tree Solution")
plt.show()

xlabels = range(step, max_operations, step)
plt.plot(xlabels, values_heap_add, label='Add')
plt.plot(xlabels, values_heap_min, label='Get Min')
plt.plot(xlabels, values_heap_max, label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Execution time (msec)")
plt.title("Performance of MinMaxHeap Solution")
plt.show()

xlabels = range(step, max_operations, step)
plt.plot(xlabels, values_binaryheap_add, label='Add')
plt.plot(xlabels, values_binaryheap_min, label='Get Min')
plt.plot(xlabels, values_binaryheap_max, label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Execution time (msec)")
plt.title("Performance of MinMaxBinaryHeap Solution")
plt.show()


plt.plot(xlabels, values_bubble_add, color='b', linestyle='-', label='Add')
plt.plot(xlabels, values_bubble_min, color='b', linestyle='--', label='Get Min')
plt.plot(xlabels, values_bubble_max, color='b', linestyle='-.', label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of Bubble Sort")
plt.show()


plt.plot(xlabels, values_binaryheap_add, color='g', linestyle='-', label='BinaryHeap Add')
plt.plot(xlabels, values_tree_add, color='r', linestyle='-', label='Tree Add')
plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Bubble Add')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of Add")
plt.show()

plt.plot(xlabels, values_binaryheap_add, color='g', linestyle='--', label='BinaryHeap Get Min')
plt.plot(xlabels, values_tree_min, color='y', linestyle='--', label='Tree Get Min')
plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min ')
plt.plot(xlabels, values_bubble_min, color='r', linestyle='--', label='Bubble Get Min')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of Get Min")
plt.show()

plt.plot(xlabels, values_binaryheap_max, color='r', linestyle='-', label='BinaryHeap Get Max')
plt.plot(xlabels, values_tree_max, color='g', linestyle='-', label='Tree Get Max ')
plt.plot(xlabels, values_heap_max, color='y', linestyle='-', label='Heap Get Max ')
plt.plot(xlabels, values_bubble_max, color='b', linestyle='-', label='Heap Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of Get Max")
plt.show()

plt.plot(xlabels, values_binaryheap_add, color='g', linestyle='-', label='BinaryHeap Get Add')
plt.plot(xlabels, values_binaryheap_min, color='g', linestyle='--', label='BinaryHeap Get Min ')
plt.plot(xlabels, values_binaryheap_max, color='g', linestyle='-', label='BinaryHeap Get Max ')
plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Get Add')

plt.plot(xlabels, values_tree_add, color='r', linestyle='-', label='Tree Get Add')
plt.plot(xlabels, values_tree_min, color='r', linestyle='--', label='Tree Get Min ')
plt.plot(xlabels, values_tree_max, color='r', linestyle='-', label='Tree Get Max ')
plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')

plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min ')
plt.plot(xlabels, values_heap_max, color='b', linestyle='-', label='Heap Get Max')
plt.plot(xlabels, values_bubble_max, color='r', linestyle='-', label='Heap Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of BinaryHeap, Tree, Bubble")
plt.show()

plt.plot(xlabels, values_binaryheap_add, color='y', linestyle='-', label='Bubble Add')
plt.plot(xlabels, values_binaryheap_min, color='y', linestyle='--', label='Bubble Get Min ')
plt.plot(xlabels, values_binaryheap_min, color='y', linestyle='-', label='Bubble Get Max')
plt.plot(xlabels, values_bubble_add, color='r', linestyle='-', label='Bubble Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Total Execution time (msec)")
plt.title("Performance of BinaryHeap, Get Max, Bubble,Get Min,Add")
plt.show()