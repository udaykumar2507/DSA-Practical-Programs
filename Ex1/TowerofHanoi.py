def TowerOfHanoi(n,src,aux,dest):
    if (n==1):
        print(src+"=>"+dest)
        return
    else:
        TowerOfHanoi(n-1,src,dest,aux)
        TowerOfHanoi(1,src,aux,dest)
        TowerOfHanoi(n-1,aux,src,dest)
TowerOfHanoi(5,'A','B','C')