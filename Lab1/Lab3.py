import random
import time


list5000 = []
listprob = [5, 2, 6, 8, 7, 11, 0, 3,9]
for i in range(5000):
    list5000.append(random.randrange(0,100))



def bubblesort(list):
    tosort = list.copy()
    tosortlength = len(tosort)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(tosortlength - 1):
            if tosort[tosortlength - i - 1] < tosort[tosortlength - i - 2]:
                sorted = False
                temp = tosort[tosortlength - i - 1]
                tosort[tosortlength - i - 1] = tosort[tosortlength - i - 2]
                tosort[tosortlength - i - 2] = temp
                #break # break odpowiada za wracanie do poczatku po zamianie
    return tosort


def selectionsort(list):
    tosort = list.copy()
    tosortlength = len(tosort)
    for i in range(tosortlength-1):
        minindex = i
        for j in range(len(tosort[i:])):
            if tosort[i+j:i+j+1].pop() < tosort[minindex]:
                minindex = j+i
        temp = tosort[i]
        tosort[i]= tosort[minindex]
        tosort[minindex]=temp
    return tosort


def quicksort(list):
    if not list:
        return []
    tosort = list.copy()
    tosortlength = len(tosort)
    index=int(tosortlength/2)
    pivot = tosort[index]
    lower = []
    higher = []
    pivots = []
    for i in range(tosortlength):
        if tosort[i]<pivot:
            lower.append(tosort[i])
        elif tosort[i]>pivot:
            higher.append(tosort[i])
        else:
            pivots.append(tosort[index])
    return quicksort(lower) + pivots + quicksort(higher)



if __name__ == '__main__':
    timebubble =time.time()
    bubblesort(list5000)
    print("BubbleSort time: ", time.time()-timebubble)

    timeselection = time.time()
    selectionsort(list5000)
    print("SelectionSort time: ", time.time() - timeselection)

    timequick = time.time()
    quicksort(list5000)
    print("QuickSort time: ", time.time() - timequick)
