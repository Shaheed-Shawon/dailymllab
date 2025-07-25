import numpy
process={
    0:3,
    1:2,
    2:1,
    3:4
}
process=dict(sorted(process.items()))

print(process)
ct=[0,0,0,0]
tat=[0,0,0,0]
wt=[0,0,0,0]
initially=0

for i in process:
    
    ct[i]=initially+process[i]
    tat[i]=ct[i]-i
    wt[i]=tat[i]-process[i]
    initially=ct[i]

print(ct)
print(tat)
print(wt)
avg_tat = sum(tat) / len(process)
avg_wt  = sum(wt)  /len(process)
print(avg_tat)
print(avg_wt)
