# -*- coding: utf-8 -*-

import csv
import codecs

"""
# maliste = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mondict = {}

with codecs.open ('./autolib.csv', 'rU', encoding = "utf-8", errors = "ignore") as csvfile:
    reader = csv.DictReader( csvfile, delimiter=';' )

    for row in reader:
        codepostal = row[ 'Postal code' ]
        if codepostal[:2] == '75':
            # maliste[ int( codepostal[3:] ) - 1 ] += int( row[ 'Cars' ] )
            if not codepostal in mondict:
                mondict[ codepostal ] = 0

            mondict[ codepostal ] += int( row[ 'Cars' ] )

# for i in maliste:
#     print( i )
print( mondict )
"""

# Methode fonctionnelle 

from itertools import groupby

def OpenCsvAsDict( path ):
    with codecs.open (path, 'rU', encoding = "utf-8", errors = "ignore") as csvfile:
        return list( csv.DictReader( csvfile, delimiter=';' ) )

reader = OpenCsvAsDict( './autolib.csv' )
filteredReader = filter( lambda x: x[ 'Postal code' ][:3] == "750", reader )
reduced = list( map( lambda x: ( x[ 'Postal code' ], x[ 'Cars' ] ), filteredReader ) )
sortedList = list( sorted( reduced, key=lambda x: x[ 0 ] ) )
grouped = groupby( sortedList, key=lambda x: x[ 0 ] )
grouped2 = list( map( lambda x: ( x[ 0 ], list( x[ 1 ] ) ), grouped ) )
final = list( map( lambda x: ( x[ 0 ], sum( map( lambda y: int( y[ 1 ] ) , x[ 1 ] ) ) ), grouped2 ) )

print( final )