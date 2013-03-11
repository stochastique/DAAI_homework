from collections import Counter
import sys
import threading

threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

def DFSLoop1(G):
    global L
    print("DFSLoop1 started ...")
    global t
    global F
    t = 0
    F = {}#range(L)
    #ind = [F.index(n) for n in range(L-1,-1,-1)]
    #print "index done"
    for i in range(L-1,-1,-1):#ind:
        print i
        if G[i][0] == False:
            DFS1(G,i)
    return F

def DFS1(G,i):
    global F
    global t
    G[i][0] = True
    for j in G[i][1]:
        if G[j][0] == False:
            DFS1(G,j)
    t += 1
    F.update({t-1:i})#F[i] = t - 1

def DFSLoop2(G,Grev):
    global s
    global leader
    global L
    s = 0
    leader = [-1]*L
    F = DFSLoop1(Grev)
    print("DFSLoop2 started ...")
    #print F
    ind=[F[k] for k in range(L-1,-1,-1)]#ind = [F.index(n) for n in range(L-1,-1,-1)]
    print "index done"
    for i in ind:
        print i
        if G[i][0] == False:
            s = i
            DFS2(G,i)
    return leader

def DFS2(G,i):
    global s
    global leader
    G[i][0] = True
    leader[i] = s
    for j in G[i][1]:
        if G[j][0] == False:
            DFS2(G,j)

def main():
    print("hello")
    f = open('SCC.txt', 'r')
    dataLines = f.readlines()
    f.close()
    global L
    #L = 16
    L = 875714

    G = list()
    for i in range(L):
        G.append([False,[]])
    for line in dataLines:
        line = line.rstrip()
        edge = line.split(" ")
        G[int(edge[0])-1][1].append(int(edge[1])-1)#second list keeps index of vertex
    print("G done")

    Grev = list()
    for i in range(L):
        Grev.append([False,[]])
    for line in dataLines:
        line = line.rstrip()
        edge = line.split(" ")
        Grev[int(edge[1])-1][1].append(int(edge[0])-1)#second list keeps index of vertex
    print("Grev done")
    
    a=DFSLoop2(G,Grev)
    c=Counter(a)
    d=c.values()
    d.sort(reverse=True)
    print d[0:5]

thread = threading.Thread(target=main)
thread.start()
