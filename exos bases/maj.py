l_good = ["A","B","C","D"]
l_wrong = ["a","B","C","d"]

def check_uppercase(l):
    """
    veritas = []
    for i in range(len(l)):
        if ord(l[i]) in range(65,91):
            veritas.append(True)        
        else:
            veritas.append(False)
    if all(veritas):
        return True
    else:
        return False
    """

    # Ou sinon en une ligne...
    return all(ord(ch) in range(65,91) for ch in l)

print ( "l_good is",check_uppercase(l_good) )
print ( "l_wrong is",check_uppercase(l_wrong) )
