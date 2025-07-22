'''pick up i -> delivery point i+n
constraint capacity: load <=Q
exact algorithm: small instance
solution: permutation of 1,2...2n -> Sol representation x[1,2...2n]=0->x[1]->x[2]->...->x[2n]->0
***Constraint:
visit[v]=True #Visited before
point i is before i+n
load: y[i] = num of packages after leaving point i
y[0]=0; y[2]=1; y[1]=2; y[5]=1; y[3]=2; y[6]=1; y[4]=0;
maintain y[i] incrementally <-> If visit pickup point load+=1
                                delivery point load-=1
y[...] -> replace by load
def Try(k):  
for v=1 -> 2n do
    if check(v,k) then
        x[k]=v 
        visit[v]=True
        f+=c[[x[k-1]][x[k]]
        if v<=n:
           load+=1
        else:
           load-=1
        if k==2*n -> Solution() #Check
        else:
           if fmin>f+cmin*(2n+1-k):
              Try(k+1)   #Branch and bound
        visit[v]=False
        f-=c[x[k-1]][x[k]]
def check(v,k):
    if visit[v]=True return False
    if v<=n and load>=Q:
        return False
    if v<=n and visit[v+n] return False
    else if v>n and visit[v-n] return False
    return True'''
import sys
def Input():
    f=sys.stdin
    [n,Q]=[int(x) for x in f.readline().split()]
    c=[]
    for _ in range(2*n+1):
        row=[int(x) for x in f.readline().split()]
        c.append(row)
    return n,Q,c
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,Q]=[int(x) for x in f.readline().split()]
        c=[]
        for _ in range(2*n+1):
            row=[int(x) for x in f.readline().split()]
            c.append(row)
    return n,Q,c
def Check(v,k):
    if visit[v]==True:
        return False
    if v<=n and load>=Q:
        return False
    if v<=n and visit[v+n]:
        return False
    elif v>n and visit[v-n]==False:
        return False
    return True
def Solution():
    global fmin
    if f+c[x[2*n]][0] <fmin:
        fmin=f+c[x[2*n]][0]
        for i in range(1,2*n+1):
            best_x[i]=x[i]
def Try(k):
    global f, load
    for v in range(1,2*n+1):
        if Check(v,k):
            x[k]=v
            visit[v]=True
            f=f+c[x[k-1]][x[k]]
            if v<=n:
                load=load+1
            else:
                load=load-1
            if k==2*n:
                Solution()
            else:
                g=f+cmin*(2*n-k+1)
                if g<fmin:
                    Try(k+1)
                else:
                    print('Ignore')
            if v<=n:
                load=load-1
            else:
                load=load+1
            f=f-c[x[k-1]][x[k]]
            visit[v]=False
            
n,Q,c=inputfile('Grab food.txt')
x=[0 for _ in range(2*n+1)]
best_x=[0 for _ in range(2*n+1)]
cmin=1e9
fmin=1e9
f=0
load=0
visit=[False for _ in range(2*n+1)]
x[0]=0
for i in range(2*n+1):
    for j in range(2*n+1):
        if i!=j:
            if cmin>c[i][j]:
               cmin=c[i][j]
Try(1)
print(fmin)  
print(n)
for i in range(1,2*n+1):
    print(best_x[i], end=' ')


            
            
    
    
        