# -*- coding: utf-8 -*-

import csv
import codecs

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