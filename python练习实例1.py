list= [1,2,3,4]
for i in list:
    for j in list:
        if i == j:
            continue
        for k in list:
            if k==j or k==i:continue
            print(i,j,k)
