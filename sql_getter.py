"""
SQL Getter
"""
import MySQLdb
from constants import SQL_ADDRESS
from constants import SQL_USER, SQL_PASS
from constants import SQL_DB

def q_team_day():
    """ SQL Function to Query the team day"""
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * FROM groups")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row)
    db.close()


def q_team_month():
    """ SQL Function to Query the team month"""
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * FROM group")
    for row in cur.fetchall():
        print(row)
    db.close()


def q_global_day():
    """ asd """
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * formoas.dasd")
    for row in cur.fetchall():
        print(row)
    db.close()

def q_global_month():
    """ asd """
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SLEC")
    for row in cur.fetchall():
        print(row)
    db.close()
