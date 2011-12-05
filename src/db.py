#!/usr/bin/python
##############################################>
##############################################>
##
##   Free BSD license 3-clause
##
##   Copyright (c)<2011>, <Martin de Bruyn>
##   All rights reserved.
##
##   Redistribution and use in source and binary forms, with or without
##   modification, are permitted provided that the following conditions are met:
##
##      - Redistributions of source code must retain the above copyright
##          notice, this list of conditions and the following disclaimer.
##      - Redistributions in binary form must reproduce the above copyright
##          notice, this list of conditions and the following disclaimer in the
##          documentation and/or other materials provided with the distribution.
##      - Neither the name of the <organization> nor the
##          names of its contributors may be used to endorse or promote products
##          derived from this software without specific prior written permission.
##
##   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
##   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
##   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
##   DISCLAIMED. IN NO EVENT SHALL <MARTIN DE BRUYN> BE LIABLE FOR ANY
##   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
##   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
##   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
#########################################################################################>
#########################################################################################>

#  Developers.

#   MJ-meo-dmt.


####>   IMPORTS   <####

# System Imports
import sys, os, random, math

# Sql import.
from sqlite3 import dbapi2 as sqlite

# Config (game)
from config import *

# Panda Imports


####>  CODE   <####

# db MainClass.

class db:
    
    
    # INIT.
    def __init__(self):
        pass 
    
    ###>
    
    ######################
    # Get planetData from sql_db.
    # This will be a basic fetchall() form sql_db.
    # getPlanetDS = getplanet Distance and Scale.
    #
    #  Using getPlanetDS:
    #   DB = db()
    #   planetData = []
    #   planetData = DB.getPlanetDS(planetData)
    #   sunData = planetData[0]
    #   print sunData[1]
    ########################
    def getPlanetDS(self, planetData):
        """
        This returns the variable 'planetData' holding a tuple, that contain 'planetDis',
        and 'planetScale' from the whole 'planetData' Table!. 
        """
        # Set the connection to the db.
        self.conn = sqlite.connect(dbPath)
         
        # Set the Cursor for This connection.
        self.cur = self.conn.cursor()
         
        # This gets 'planetDis' and 'planetScale' from the database.
        self.cur.execute("select planetDis, planetScale from planetData order by planetID")
         
        # Lets store the data in a var.
        planetData = self.cur.fetchall()
         
        # Close the Cursor and Connection.
        self.cur.close()
        self.conn.close()
         
        # Return the Var. with the data from the sql_db.
        # Ready for slicing...
        return planetData
         
    ###>
    
    def savePlayer(self, playerID):
        """
        This is a basic playerData save method.
        !Needs work!
        """        
        # Set the connection to the db.
        self.conn = sqlite.connect(dbPath)
        
        # Setup cursor for the Connection.
        self.cur = self.conn.cursor()
        
        # Execute "string" - This saves all the playerData (playerName, playerPos, playerCargo e.g)
        # Also this is very basic i guess... 
        
        # PlayerID var.
        playerid = playerID
        
        # Delete the old sql entry and then commit the new one.
        self.cur.execute("delete from playerData where playerID=playerid")
        
        # Insert the new data.
        self.cur.execute("insert into playerData(playerName, playerPos) values (?, ?)", (playerName, playerPos))
        
        # Commit/save the data.
        self.conn.commit()
        
        # Close the Cursor and the Connection.
        self.cur.close()
        self.conn.close()
        
    ###>






















