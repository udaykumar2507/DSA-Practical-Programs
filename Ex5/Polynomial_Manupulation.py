def add(poly1,poly2):
    max_len=max(len(poly1),len(poly2))
    res=[0]*max_len
    for i in range(len(poly1)):
        res[i]+=poly1[i]
    for i in range(len(poly2)):
        res[i]+=poly2[i]
    return res
def mul(poly1,poly2):
    max_len=len(poly2)+len(poly1)-1
    res=[0]*max_len
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            res[i+j]=poly1[i]*poly2[j]
    return res
def display_polynomial(poly):
    terms=[]
    for degree,coeff in enumerate(poly):
        if (coeff!=0):
            terms.append(f"{coeff}x^{degree}")
        if not terms:
            return "0"
    return "+".join(terms)
sum1=add([2,0,1],[1,3])
print(display_polynomial(sum1))    

