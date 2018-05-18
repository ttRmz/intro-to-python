def max_with_index(l):

    i = 0
    pos, max = 0,0

    while i < len(l):
        if l[i]>max:
            pos, max= i, l[i]
        i = i+1

    return {'max' : max, 'indice' : i}


print( max_with_index([2,4,8,1,11])['max'] )