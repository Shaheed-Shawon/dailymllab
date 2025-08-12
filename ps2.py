process = {
    2: [0, 11],
    0: [5, 28],
    3: [12, 2],
    1: [2, 10],
    4: [9, 16]
}

# priority: key
# values: [arrival_time, burst_time]

process_list = []
for priority, (at, bt) in process.items():
    process_list.append({'priority': priority, 'arrival': at, 'burst': bt})

process_list.sort(key=lambda x: (x['arrival'], x['priority']))

n = len(process_list)
completed = 0
current_time = 0
result = []

while completed < n:
   
    arrived = [p for p in process_list if p['arrival'] <= current_time and 'start' not in p]
    if not arrived:
        current_time += 1
        continue

  
    arrived.sort(key=lambda x: x['priority'])
    proc = arrived[0]
    proc['start'] = current_time
    proc['finish'] = proc['start'] + proc['burst']
    proc['waiting'] = proc['start'] - proc['arrival']
    proc['turnaround'] = proc['finish'] - proc['arrival']
    current_time = proc['finish']
    completed += 1
    result.append(proc)

result.sort(key=lambda x: x['priority'])

print("PID  Arrival   Burst     Priority  Start     Finish    Waiting     Turnaround  ")
for p in result:
    print(f"p{p['priority']+1:<4} {p['arrival']:<9} {p['burst']:<9} {p['priority']:<9} {p['start']:<9} {p['finish']:<9} {p['waiting']:<10} {p['turnaround']:<10}")

avg_waiting = sum(p['waiting'] for p in result) / n
avg_turnaround = sum(p['turnaround'] for p in result) / n

print(f"\nAverage Waiting Time: {avg_waiting:.1f}")
print(f"Average Turnaround Time: {avg_turnaround:.1f}")
