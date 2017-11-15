for i in range(1,5):
    for j in range(1,5):
        if (j==i):
            continue;
        for k in range(1,5):
            if (k==i or k==j):
                continue;
            print(i,j,k)
