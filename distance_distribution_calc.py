def distance_distr(n):
    l0 = [(0, 0)]
    l1 = [2**n]
    diff_dic = {0: l1[0] % 2}
    stab = (max(l1) <= 1)
    largest = 1
    while (not stab):
        l2 = [l1[0]//2]
        l3 = [(l0[0][0]+1, l0[0][1])]
        for i in range(1, len(l1)):
            l2.append(l1[i]//2 + l1[i-1]//2)
            l3.append((l0[i][0] +1, l0[i][1]))
        l2.append(l1[len(l1)-1]//2)
        l3.append((l0[len(l1)-1][0], l0[len(l1)-1][1]+1))
        l1 = l2
        l0 = l3
        stab = (max(l1) <= 1)
        if l1[0] == 0:
            l1 = l1[1:]
            l0 = l0[1:]
        if l1[-1] == 0:
            l1 = l1[:len(l1)-1]
            l0 = l0[:len(l0)-1]
        for i in range(len(l0)):
            if (not ((l0[i][1]-l0[i][0]) in diff_dic.keys())):
                diff_dic[l0[i][1]-l0[i][0]] = (l1[i] % 2)
            else:
                diff_dic[l0[i][1]-l0[i][0]] = diff_dic[l0[i][1]-l0[i][0]] + (l1[i] % 2)
    diff_final = sorted([(k, diff_dic[k]) for k in diff_dic.keys()])
    diff_final2 = [d[1] for d in diff_final]
    return diff_final2
for n in range(16):
    print(distance_distr(n))
