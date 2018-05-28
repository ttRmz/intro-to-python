maListe = [-2,4,3,-5,8,3]

def triCroissant(l):
    for i in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
    return l

print(triCroissant(maListe))