
# COPAS QUICK SORT
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first][0]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark][0] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark][0] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

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



#NGODINGNYA DARI SINI

import math as m
f = open("ganteng.csv","r")
a = f.readlines()

# FOLD ARRAY
def foldarray(arr,testong):
    arraytraining = []
    arraytesting = []
    for i in range(len(arr)):
        s = arr[i].split(',')
        if (int(s[4]) == testong):
            arraytesting.append(arr[i])
        elif int(s[4]) == 4:
            pass
        else:
            arraytraining.append(arr[i])
    return [arraytraining,arraytesting]

folded = foldarray(a,4)


def euclidean(x1,y1,x2,y2):
    deltax = abs(float(x2)-float(x1))
    # print deltax
    # print deltax
    deltay = abs(y2-y1)
    deltax = float(deltax) ** 2
    deltay = float(deltay) ** 2
    return m.sqrt(deltax+deltay)



def euclidab(x1,y1,source,a,b):
    x = []
    for i in range(a,b):
        s = source[i].split(',')
        x2 = float(s[1])
        y2 = float(s[2])
        nilai = euclidean(x1,y1,x2,y2)
        x.append([nilai,s[3].replace('\n','').replace('\r',''),i+1])
    # print i
    quickSort(x)
    return x

def getresultinK(arr,K):
    ya = 0
    tidak = 0
    for i in range(0,K):
        decision = arr[i][1]
        if (decision == "Ya") :
            ya = ya + 1
        else:
            tidak = tidak + 1
    # print ya, tidak
    if (ya >= tidak):
        return "Ya"
    else:
        return "Tidak"





testing = []
for i in range(0,5):
	testing.append(a[i])

evaluasi = []
for i in range(5,15):
	evaluasi.append(a[i])

for i in range(len(testing)):
	s = testing[i].split(',')
	x1 = float(s[1])
	y1 = float(s[2])
	hasileuclidean = euclidab(x1, y1, evaluasi, 0, len(evaluasi))
	print getresultinK(hasileuclidean, 5)
	print hasileuclidean




def foldarray(arr,K):
    panjang = len(arr)
    s = m.floor(panjang/K)

    

#
# s = a[0].split(',')
# x1 = float(s[1])
# y1 = float(s[2])
# s = a[5].split(',')
# x2 = float(s[1])
# y2 = float(s[2])
# print x1,y1,x2,y2
# print euclidean(x1,y1,x2,y2)
# print x1, x2, y1, y2
# print euclidean(x1,x2,y1,y2)

