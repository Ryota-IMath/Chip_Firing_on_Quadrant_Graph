def print_table(n):
    l1 = [2**n]
    print(l1[0])
    stab = (max(l1) <= 1)
    while (not stab):
        l2 = [l1[0]//2]
        for i in range(1, len(l1)):
            l2.append(l1[i]//2 + l1[i-1]//2)
        l2.append(l1[len(l1)-1]//2)
        l1 = l2
        stab = (max(l1) <= 1)
        if l1[0] == 0:
            l1 = l1[1:]
        if l1[-1] == 0:
            l1 = l1[:len(l1)-1]
        out_str = ""
        for i in l1:
            out_str = out_str + str(i)+" "
        print(out_str)
print_table(9)
