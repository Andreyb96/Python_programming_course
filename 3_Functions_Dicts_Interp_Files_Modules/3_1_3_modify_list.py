def modify_list(l):
    for x in range(len(l)-1,-1,-1):
        if (l[x]%2==0):
            l[x] = int(l[x]/2)
        else:
            l.remove(l[x])
