def total_firings(n):
    l1 = [2**n]
    stab = (max(l1) <= 1)
    fire_count=0
    while not stab:
        l2 = [l1[0]//2]
        fire_count +=l1[0]//2
        for i in range(1, len(l1)):
            l2.append(l1[i]//2 + l1[i-1]//2)
            fire_count += l1[i]//2
        l2.append(l1[len(l1)-1]//2)
        l1 = l2
        stab = (max(l1) <= 1)
        if l1[0] == 0:
            l1 = l1[1:]
        if l1[-1] == 0:
            l1 = l1[:len(l1)-1]
    return fire_count
sequence_total = ""
for n in range(28):
    sequence_total = sequence_total + str(total_firings(n)) + ", "
print(sequence_total)
