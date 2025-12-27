def difference_table(n):
    l1 = [2**n]
    print(str(2**n) + " " + str(2**n))
    stab = False
    while not stab:
        l2 = [l1[0]//2]
        for i in range(1, len(l1)):
            l2.append(l1[i]//2 + l1[i-1]//2)
            l2.append(l1[len(l1)-1]//2)
        l1 = l2
        s1 = set(l1)
        if not (s1-set([1, 0])):
            stab = True
        if l1[0] == 0:
            l1 = l1[1:]
        if l1[-1] == 0:
            l1 = l1[:len(l1)-1]
        l5 = [l1[0]]+ [abs(t - s) for s, t in zip(l1, l1[1:])] + [l1[-1]]
        str_out = ""
        for s in l5:
            str_out = str_out + str(s) +" "
        print(str_out)
        row_count+= 1
difference_table(9)
