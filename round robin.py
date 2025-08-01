pid = [1, 2, 3]
at = [0, 1, 2]
bt = [10, 4, 5]
q = 2
n = len(pid)
rt = bt[:]
ct = [0] * n
t = 0
done = 0
rq = []

while done < n:
    for i in range(n):
        if at[i] <= t and rt[i] > 0 and i not in rq:
            rq.append(i)
    if rq:
        i = rq.pop(0)
        run = min(q, rt[i])
        t += run
        rt[i] -= run
        if rt[i] == 0:
            ct[i] = t
            done += 1
        else:
            rq.append(i)
    else:
        t += 1

tat = [ct[i] - at[i] for i in range(n)]
wt = [tat[i] - bt[i] for i in range(n)]

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

print("CT:", ct)
print("TAT:", tat)
print("WT:", wt)
print("Avg CT:", sum(ct) / n)
print("Avg TAT:", avg_tat)
print("Avg WT:", avg_wt)
