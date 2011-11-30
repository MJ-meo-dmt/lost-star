##########################################
###									######
###		THE VOID					######
###		PROJECT : lost-star			######
###		0x7dc 'EDEN'				######
###									######
##########################################
# Start: early Oct. 2011

# DEVELOPERS

# 	* MJ-me0-dmt  - 1

#-->

# License
'''
Free BSD license 3-clause

Copyright (c)<2011>, <Martin de Bruyn>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    - Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    - Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    - Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

#-->

# Engine imports

# CORE

# TASK

# PANDAC

# DIRECT

# EXTRA
import random, sys, os, math
from sqlite3 import dbapi2 as sqlite

##
# Game Imports
#
from config import *

###########################
########## CODE ###########
##########################


class dbMain:
    
    
    
    def __init__(self):
        
        # Print Init.
        print ""
        print "#####################################"
        print "--  DB LOADED --"
        print ""
        
        
    
    # Return the sql request data.
    def getPlanetData(self, PID, COL1, COL2, COL3): # COL
        """Returns the value requested by the params, PID + COL1 -> 3
            PID = PlanetID. (int value)
            COL1 to 3 = Column Name in db. (str value) check config.
            Fetch one value at a time.
        """
        # Get connection to db.
        self.conn = sqlite.connect(db_path)
        
        # Set cursor.
        self.cur = self.conn.cursor()
        
        # Send request for planetID, COL=str, PID=int.
        #self.sqlQ = "select %s from planetData where planetID = '%d'" % (COL, PID)
        self.sqlQ = "select %s, %s, %s from planetData where planetID = '%d'" % (COL1, COL2, COL3, PID)
        
        
        # Checking.
        #print "COL VALUE: '"+ COL+ "'"
        print "PID VALUE: '%d'" % (PID)
        print "---------------------------->>>"
        
        self.cur.execute(self.sqlQ) 
        print "cur.execute -- DONE"
        
        self.planetData1 = self.cur.fetchone()
        print "cur.fetchone - 1 -- DONE"
        
        self.planetData2 = self.cur.fetchone()
        print "cur.fetchone - 2 -- DONE"
        
        self.planetData3 = self.cur.fetchone()
        print "cur.fetchone - 3 -- DONE"
        
        return self.planetData1, self.planetData2, self.planetData3
        print "planetData return -- DONE"
        
        #self.conn.commit() # This method doesn't commit anything.
        #self.conn.close() # Best if we remove it from here and use it after data has been retrieved with in code.




# Testing part

db = dbMain()
# Param: planetID, COL Id0 - > 2 check config
planetData = db.getPlanetData(6, COL0, COL1, COL2)[0]
# slice it by 0 --> 2 (0=planetName[TEXT], 1=planetDis[REAL]}, 2=planetScale[REAL])
checkFloat = planetData[2]

print "Float: ", checkFloat
print "Get Test: "+ str(planetData[0])

mercuryData = db.getPlanetData(2, COL0, COL1, COL2)[0]

print mercuryData[2]




