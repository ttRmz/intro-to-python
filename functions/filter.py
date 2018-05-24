tup = ( 1,2,3,4,5,6,7,8,9 )

def isOdd( nb ):
    return nb % 2 != 0

def monFiltre( func, tupp ):
    for i in tupp:
        if func( i ):
            yield i

print( list( monFiltre( isOdd, tup ) ) )
print( list( filter( isOdd, tup ) ) )
print( list( filter( lambda x: x % 2 != 0, tup ) ) )