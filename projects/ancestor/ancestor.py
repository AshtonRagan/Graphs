
def earliest_ancestor(ancestors, starting_node):

    l = [2]
    d = {}
    q = ancestors
    for i in q:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]

    for i in d:
        for j in d[i]:
            # print(l)
            if j == l[0]:
                l.append(i)

    print(l)


# {1: [3], 2: [3], 3: [6], 5: [6, 7], 4: [5, 8], 8: [9], 11: [8], 10: [1]}
a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
     (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(a, 1)
