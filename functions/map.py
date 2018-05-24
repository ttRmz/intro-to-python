# map
tup = ( 1,2,3,4,5 )

def moinsTrois( nb ):
    return nb - 3

def retireTrois( tupp ):
    tmp = []
    for i in tupp:
        tmp.append( moinsTrois( i ) )
    return tmp

def retireTrois2( tupp ):
    for i in tupp:
        yield moinsTrois( i )

def monMap( func, tupp ):
    for i in tupp:
        yield func( i )

print( list( map( moinsTrois, tup ) ) )
print( list( map( lambda x: x - 3, tup ) ) )
print( list( retireTrois( tup ) ) )
print( list( retireTrois2( tup ) ) )
print( list( monMap( moinsTrois ,tup ) ) )