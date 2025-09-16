def lcal(reqseq, h):
    total = 0
    ch = h
    
    while ch > 0:
        total += reqseq[ch] - reqseq[ch - 1]
        print("Moving left to:", reqseq[ch - 1], "Total:", total)
        ch -= 1
    
    while ch < len(reqseq) - 1:
        total += reqseq[ch + 1] - reqseq[ch]
        print("Moving right to:", reqseq[ch + 1], "Total:", total)
        ch += 1
    
    print("Total head movement (left direction):", total)
    return total

def rcal(reqseq, h):
    total = 0
    ch = h
    
    while ch < len(reqseq) - 1:
        total += reqseq[ch + 1] - reqseq[ch]
        print("Moving right to:", reqseq[ch + 1], "Total:", total)
        ch += 1
    
    while ch > 0:
        total += reqseq[ch] - reqseq[ch - 1]
        print("Moving left to:", reqseq[ch - 1], "Total:", total)
        ch -= 1
    
    print("Total head movement (right direction):", total)
    return total

reqseq_input = input("Enter the request sequence numbers separated by space: ")
reqseq = list(map(int, reqseq_input.strip().split()))

head = int(input("Enter the initial head position: "))

reqseq.sort()

if head not in reqseq:
    reqseq.append(head)
    reqseq.sort()

h = reqseq.index(head)

direction = input("Enter direction (left or right): ").strip().lower()

if direction == "left":
    total = lcal(reqseq, h)
elif direction == "right":
    total = rcal(reqseq, h)
else:
    print("Invalid direction entered. Please enter 'left' or 'right'.")
