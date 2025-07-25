import numpy
process={
    0:5,
    1:2,
    2:1,
    3:4
}
arrival=[0,1,2,3]
burst=[process[i] for i in range(len(process))]
n=len(process)
ct=[0]*n
tat=[0]*n
wt=[0]*n
initially=0
done=[0]*n

for _ in range(n):
    idx=-1
    shortest=9999
    for i in range(n):
        if arrival[i]<=initially and not done[i] and burst[i]<shortest:
            shortest=burst[i]
            idx=i
    if idx==-1:
        initially+=1
        continue
    ct[idx]=initially+burst[idx]
    tat[idx]=ct[idx]-arrival[idx]
    wt[idx]=tat[idx]-burst[idx]
    initially=ct[idx]
    done[idx]=1

print(ct)
print(tat)
print(wt)
avg_tat = sum(tat) / n
avg_wt  = sum(wt)  / n
print(avg_tat)
print(avg_wt)
