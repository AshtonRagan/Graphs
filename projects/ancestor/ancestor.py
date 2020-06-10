
def earliest_ancestor(ancestors, starting_node):

    l = [starting_node]
    d = {}
    q = ancestors
    a = None
    for i in q:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]

    while len(l) > 0:
        # print("a", a)
        for i in d:
            # print("L: ", l)
            for j in d[i]:
                if j == l[0]:
                    if len(l) >= 2:
                        # print("LEN: ", len(l))
                        if i > l[1]:
                            # print("I: ", i, "L[1]: ", l[1])
                            l.insert(1, i)
                        else:
                            l.append(i)
                    else:
                        l.append(i)
        a = l.pop(0)

    if a == starting_node:
        return -1
    else:
        return a
    # print(l)


# {1: [3], 2: [3], 3: [6], 5: [6, 7], 4: [5, 8], 8: [9], 11: [8], 10: [1]}
# a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


# print(earliest_ancestor(a, 8))
