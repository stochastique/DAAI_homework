print("hello")
f = open('IntegerArray.txt', 'r')
data_str = f.read()
f.close()
data_lst = data_str.split('\n')
data = map(int, data_lst)

ldata = list()
for l in range(len(data)):
    ldata.append([data[l]])

## L is list of lists
def mergesort(L,Count):
    if len(L) == 1:
        return [L,Count]
    else:
        newL = list()
        for l in range(0,len(L),2):
            C = list()
            i = 0
            j = 0
            A = L[l]
            if l+1 < len(L):
                B = L[l+1]
                for k in range(len(A)+len(B)):
                    if ((i < len(A) and j == len(B)) or
                        (i < len(A) and A[i] < B[j])):
                        C.append(A[i])
                        i = i + 1
                    elif ((j < len(B) and i == len(A)) or
                          (j < len(B) and B[j] < A[i])):
                        C.append(B[j])
                        j = j + 1
                        Count = Count + len(A) - i
                newL.append(C)
            elif l+1 == len(L):
                newL.append(A)
        return mergesort(newL,Count)

L = list([10,2,3,11,23,22,4,1,5,7,17,6])
LL = list()
for l in range(len(L)):
  LL.append([L[l]])

a = mergesort(ldata,0)
print(a[-1])
