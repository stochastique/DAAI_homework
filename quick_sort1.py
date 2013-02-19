print('hello!')
f = open('QuickSort.txt', 'r')
data_str = f.read()
f.close()
data_lst = data_str.split('\n')
data = map(int, data_lst)
print(len(data))
M = 0

def quicksort(A,l,r):
    global M
    if len(A) == 1:
        return A
    elif len(A) == 0:
        return []
    else:
        M = M + len(A) - 1
        p = A[l]
        i = l + 1
        for j in range(l+1,r):
            if A[j] < p:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
                i = i + 1
        tmp = A[l]
        A[l] = A[i-1]
        A[i-1] = tmp
        return quicksort(A[l:i-1],0,len(A[l:i-1]))+[A[i-1]]+quicksort(A[i:],0,len(A[i:]))

a = [5,1,4,8,3,6,2,7,13,9,10,12,11]

S = quicksort(data,0,len(data))
