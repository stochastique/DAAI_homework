import random

print("hello")
f = open('kargerMinCut.txt', 'r')
dataLines = f.readlines()
f.close()

dataList = list()
for line in dataLines:
    line = line.rstrip()
    dataList.append([int(n) for n in line.split('\t')[1:]])

adjMatrix = [[0L for col in range(200)] for row in range(200)]
i = 0
for line in dataLines:
    line = line.rstrip()
    indx = [int(n) for n in line.split('\t')[1:]]
    for j in indx:
        adjMatrix[i][j-1] = 1L
    i += 1

def t(M):
    return map(list, zip(*M))

def e(M):
    edgesList = list()
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            if M[i][j]:
                edgesList.append([i,j,M[i][j]])
    return edgesList

def r(M,edg):
    M[edg[0]] = map(sum,t([M[edg[0]],M[edg[1]]]))
    M = t(M)
    M[edg[0]] = map(sum,t([M[edg[0]],M[edg[1]]]))
    M[edg[0]][edg[0]] = 0
    del M[edg[1]]
    M = t(M)
    del M[edg[1]]
    return M

def rand_c(weights):
    T = []
    i = 0

    for w in weights:
        i += w
        T.append(i)

    rnd = random.random() * i
    for n, k in enumerate(T):
        if rnd < k:
            return n

        
m = [[0,1,1,0,1],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def experiment(M):
    while len(M) > 2:
        edgesL = e(M)
        w = [edge[2] for edge in edgesL]
##        try:
##            w = [x/float(sum(w)) for x in w]
##        else:
##            print('Dividing by zero!')
        M = r(M,edgesL[rand_c(w)])
    return M

print experiment(adjMatrix)
