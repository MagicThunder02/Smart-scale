#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import datetime


class classToday:

    def actualday(self):
        i = datetime.date.today()
        print(i)
        i = str(i)
        # i = i.split('-')
        # return(i[2])
        return(i)


class classSSdb:
    day = classToday()
    db = mdb.connect('localhost', 'root', 'root', 'smart-scale')
    cursor = db.cursor()

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
                print("%d, %s, %d, %f") % (id, datetime, user_id, weight)
        except:
            print("Error: unable to fecth data")
            sys.exit(1)

        # --------------------------------------------------------------------
    def insert(self):
        sql = "INSERT INTO weights(datetime, user_id, weight) VALUES (" + self.day.actualday() + ", 1, 75)"
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()


DB = classSSdb()
DB.listWeights()
DB.insert()
