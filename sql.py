"""
SQL Getter
"""
import MySQLdb
from constants import SQL_ADDRESS
from constants import SQL_USER, SQL_PASS
from constants import SQL_DB


class SqlGetter(object):
    """docstring for SqlGetter"""
    def __init__(self):
        self.ip = SQL_ADDRESS
        self.us = SQL_USER
        self.pw = SQL_PASS
        self.dba = SQL_DB
        self.db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                                  user=SQL_USER,         # your username
                                  passwd=SQL_PASS,  # your password
                                  db=SQL_DB)        # name of the data base
        self.cur = self.db.cursor()


    def q_team_day(self):
        """ SQL Function to Query the team day"""
        self.cur.execute("SELECT * FROM group")

        # print all the first cell of all the rows
        for row in self.cur.fetchall():
            print(row)
        self.co_close()


    def q_team_month(self):
        """ SQL Function to Query the team month"""
        self.cur.execute("SELECT * FROM group")
        for row in self.cur.fetchall():
            print(row)
        self.co_close()


    def q_global_day(self):
        """ asd """
        self.cur.execute("SELECT * formoas.dasd")
        for row in self.cur.fetchall():
            print(row)
        self.co_close()

    def q_global_month(self):
        """ asd """
        self.cur.execute("SLEC")
        for row in self.cur.fetchall():
            print(row)
        self.co_close()


    def co_close(self):
        """docstring for SqlGetter"""
        self.db.close()
