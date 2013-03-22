print("hello")
f = open('dijkstraData.txt', 'r')
dataLines = f.readlines()
f.close()

dataList = list()
for line in dataLines:
    line = line.rstrip()
    dataList.append([v for v in line.split('\t')[1:]])
dataDict = {}
for s in range(len(dataList)):
    for i in range(len(dataList[s])):
        v = dataList[s][i].split(',')
        dataList[s][i] = [int(v[0])-1,int(v[1])]
        
X = set([0])
V = set(range(200)) - X
A = dict({0:0})
while V:
    d = {}
    for v in X:
        for i in range(len(dataList[v])):
            if dataList[v][i][0] in V:
                w = dataList[v][i][0]
                d.update({A[v]+dataList[v][i][1]:[v,w]})
    A.update({d[min(d)][1]:min(d)})
    X = X | set([d[min(d)][1]])
    V = V - set([d[min(d)][1]])

print A[6],A[36],A[58],A[81],A[98],A[114],A[132],A[164],A[187],A[196]
