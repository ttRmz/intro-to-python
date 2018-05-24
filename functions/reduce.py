from functools import reduce
tup = ( 1,2,3,4,5,6,7,8,9 )
tup2 = ( "a", "b", "c" )

# print( sum( tup ) + ( len( tup ) - 1 ) * 2 )
# print( reduce( lambda a, x:  a * x, tup ) )
print( reduce( lambda a, x:  a + x, tup ) )
print( reduce( lambda a, x:  a * x, tup ) )
print( reduce( lambda a, x:  a + x, tup2 ) )

res = 0
for i in tup:
    res += i

print( res )