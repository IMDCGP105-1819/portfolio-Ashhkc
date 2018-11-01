def removeDups(L1, L2):
    for e in range(len(L1)):
        print(e)
        if L1[e] in L2:
             L1.remove(L1[e])
             e = e - 1

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print(L1)
print(L2)
