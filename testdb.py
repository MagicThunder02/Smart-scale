#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import datetime
import time


class classTimeUtilities:

    def actualtime(self):
        # We print timestamp in the following format: Y-m-d H:M:S
        tm = time.time()
        print(datetime.datetime.fromtimestamp(tm).strftime("%Y/%m/%d %H:%M:%S"))
        return(tm)

class classSSdb:
    day = classTimeUtilities()
    db = mdb.connect('localhost', 'root', 'root', 'smart-scale')
    cursor = db.cursor()
    arrayweights = []
    arraydates = []

    def __init__(self):
        pass
    # --------------------------------------------------------------------
    def listWeights(self):
        try:
            # Execute the SQL command
            self.cursor.execute("SELECT * FROM weights")
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            for row in results:
                id = row[0]
                datetime = row[1]
                user_id = row[2]
                weight = row[3]
                # Now print fetched result
                print("%d, %d, %d, %f") % (id, datetime, user_id, weight)
        except Exception as sql_error:
            print("Error: unable to fecth data")
            sys.exit(1)

    # ---------------------------------------------------------------------

    def weights_dates(self):
       # try:
            # Execute the SQL command
            self.cursor.execute("SELECT weight, datetime FROM weights")
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            results = list(sum(results, ()))
            print(results)
            for i in range(0, len(results), 2):
              tmp = results[i]
              self.arrayweights.append(tmp)
                         
            for j in range(1, len(results), 2):
               tmp = datetime.datetime.fromtimestamp(results[j]).strftime("%d")
               self.arraydates.append(int(tmp))
            
 
            
       # except Exception as sql_error:
          #  print("Error: unable to fecth data")
          #  sys.exit(1)
            '''
    def onlydates(self):
        try:
            # Execute the SQL command
            self.cursor.execute("SELECT 'datetime' FROM weights")
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            tm = time.time()
            results = str(datetime.datetime.fromtimestamp(tm).strftime("%Y/%m/%d %H:%M:%S"))
            self.arraydates.append(results[9] + results[10])
        except Exception as sql_error:
            print("Error: unable to fecth data")
            sys.exit(1)
            '''
        # --------------------------------------------------------------------

    def insert(self, weight):
        tm = self.day.actualtime()
        sql = "INSERT INTO weights(datetime, user_id, weight) VALUES ({}, 1, {})".format(tm, weight)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('OK!')    
        except Exception as sql_error:
            print('ERROR')
            print(sql_error)
            self.db.rollback()


# DB = classSSdb()
# DB.listWeights()
# DB.insert()
