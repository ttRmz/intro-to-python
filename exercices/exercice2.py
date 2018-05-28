text="aaabbhhdddcccjjhhggffqqllkki iooouuurrrrppppqqqooo   okkk llllooooppprrrr tttt ZZzzzz"

def dico(txt):
    D = {}
    for i in range(len(txt)):
        lettre = txt[i].lower()
        if lettre != ' ':
            if not lettre in D:
                D[ lettre ] = 0
            D[ lettre ] += 1
    return D

print( dico(text) )