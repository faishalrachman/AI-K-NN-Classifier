# COPAS QUICK SORT
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first][0]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark][0] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark][0] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# NGODINGNYA DARI SINI

import math as m

f = open("ganteng.csv", "r")
a = f.readlines()


def euclidean(x1, y1, x2, y2):
    deltax = abs(float(x2) - float(x1))
    # print deltax
    # print deltax
    deltay = abs(y2 - y1)
    deltax = float(deltax) ** 2
    deltay = float(deltay) ** 2
    return m.sqrt(deltax + deltay)


def euclidab(x1, y1, source, a, b):
    x = []
    for i in range(a, b):
        s = source[i].split(',')
        x2 = float(s[1])
        y2 = float(s[2])
        nilai = euclidean(x1, y1, x2, y2)
        x.append([nilai, s[3].replace('\n', '').replace('\r', ''), s[0]])
    # print "Nilai X sebelum di sorting : ", x
    quickSort(x)
    # print "Nilai X sesudah di sorting : ", x
    return x


def getresultinK(arr, K):
    ya = 0
    tidak = 0
    for i in range(0, K):
        decision = arr[i][1]
        if (decision == "Ya"):
            ya = ya + 1
        else:
            tidak = tidak + 1
    # print ya, tidak
    if (ya >= tidak):
        return "Ya"
    else:
        return "Tidak"


def hitungArray(x, y, z, K, a):
    # hasil = []
    evaluasi = []
    for i in range(x, y):
        evaluasi.append(a[i])
    training = []
    for i in range(0, x):
        training.append(a[i])
    for i in range(y, z):
        training.append(a[i])

    # print training
    for i in range(len(evaluasi)):
        s = evaluasi[i].split(',')
        x1 = float(s[1])
        y1 = float(s[2])
        hasileuclidean = euclidab(x1, y1, training, 0, len(training))
        x = hasileuclidean.__getslice__(0,5)
        print "Data ke-", s[0]
        print "Hasil : ", getresultinK(hasileuclidean,1), getresultinK(hasileuclidean,3), getresultinK(hasileuclidean,5)
        for i in range(len(x)):
            print x[i][2],"\t", x[i][0] ,"\t" ,  x[i][1]
        # hasil.append(getresultinK(hasileuclidean, K))
        # print getresultinK(hasileuclidean,K), hasileuclidean.__getslice__(0,K)
    # return hasil

# def gantengArray(array,panjangarray,kfold,knn):
#     upil = []
#     awal = 0
#     panjangkfold = len(array)/kfold
#     for i in range(0,kfold-1):
#         upil.extend(hitungArray(awal,awal+panjangkfold,panjangarray,knn,array))
#         print awal, awal+panjangkfold-1,panjangarray,knn,array
#         awal = awal+panjangkfold-1
#     return upil
#
# hitung = gantengArray(a,15,5,1)
# for i in range(0,15):
#     print hitung[i]

hitungArray(0,3,15,1,a)
hitungArray(3,6,15,1,a)
hitungArray(6,9,15,1,a)
hitungArray(9,12,15,1,a)
hitungArray(12,15,15,1,a)
hitungArray(15,20,15,1,a)