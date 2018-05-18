import random
import time


list5000 = []
list100 = []
listprob = [5, 2, 6, 8, 6, 11, 0, 3]
for i in range(5000):
    list5000.append(random.randrange(0,100))
listprzyklad = [2,4,1,3]


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
    sorted = False
    while not sorted:
        sorted = True
        for i in range(tosortlength-1):
            minindex = i
            for j in range(len(tosort[i:])):
                if tosort[i+j:i+j+1].pop() < tosort[minindex]:
                    minindex = j+i
            temp = tosort[i]
            tosort[i]= tosort[minindex]
            tosort[minindex]=temp
            #print(minindex, "  LICZBA w liscie ", tosort[minindex], "   ", tosort)
    return tosort


def quicksort(list):
    tosort = list.copy()
    tosortlength = len(tosort)
    return tosort


if __name__ == '__main__':
    timebubble =time.time()
    print(bubblesort(list5000))
    print("BubbleSort time: ", time.time()-timebubble)

    timeselection = time.time()
    print(selectionsort(list5000))
    print("SelectionSort time: ", time.time() - timeselection)

    timequick = time.time()
    print(quicksort(list5000))
    print("QuickSort time: ", time.time() - timequick)
