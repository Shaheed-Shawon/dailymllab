import numpy


process = {
    0: [5, 2],
    1: [2],
    2: [1],
    3: [4]
}


arrival = []
burst = []
pid = 0
for key in sorted(process.keys()):
    for b in process[key]:
        arrival.append(key)
        burst.append(b)
        pid += 1

n = len(arrival)
ct = [0]*n
tat = [0]*n
wt = [0]*n
initially = 0
done = [0]*n

for _ in range(n):
    idx = -1
    shortest = 9999
    for i in range(n):
        if arrival[i] <= initially and not done[i] and burst[i] < shortest:
            shortest = burst[i]
            idx = i
    if idx == -1:
        initially += 1
        continue
    ct[idx] = initially + burst[idx]
    tat[idx] = ct[idx] - arrival[idx]
    wt[idx] = tat[idx] - burst[idx]
    initially = ct[idx]
    done[idx] = 1

print("CT:", ct)
print("TAT:", tat)
print("WT:", wt)

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n
print("Average TAT:", avg_tat)
print("Average WT:", avg_wt)
