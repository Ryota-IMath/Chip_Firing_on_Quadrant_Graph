def generate_and_count_rows(n):

    l1 = [2**n]
    print(l1)
    stab = not (n > 0)

    layer_count = 1

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
        print(l1)

        layer_count+= 1

    return layer_count
# We print the F(x, y) table for n=0,1, ..., 27 and then we print the number of nonzero rows.

for i in range(28):

    print(generate_and_count_rows(i))
