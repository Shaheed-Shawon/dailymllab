def find_nearest(requests, current_head):
    min_distance = float('inf')
    nearest = None
    for request in requests:
        distance = abs(current_head - request)
        if distance < min_distance:
            min_distance = distance
            nearest = request
    return nearest


input_string = input("Enter integers separated by spaces: ")
requests = list(map(int, input_string.split()))


requests.sort()


head = int(input("Enter the initial head position: "))

total_seek_time = 0
current_head = head

while requests:
    nearest = find_nearest(requests, current_head)
    seek_time = abs(current_head - nearest)
    total_seek_time += seek_time
    current_head = nearest
    requests.remove(nearest)

print("Total seek time:", total_seek_time)
