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

    a = []
    for row in cur.fetchall():
        print(row)
        a.append(row)
    db.close()
    return a


def q_team_month():
    """ SQL Function to Query the team month"""
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("select Group_group_id, SUM(env_impact) from activity_history, nfc_card, activity where nfc_card_nfc_id=nfc_id and activity.activity_id=nfc_card.activity_activity_id GROUP BY Group_group_id ORDER BY SUM(env_impact) ASC;")
    # cur.execute("SELECT * FROM group")
    # return cur
    a = []
    for row in cur.fetchall():
        print(row)
        a.append(row)
    db.close()
    return a

def q_global_day():
    """ asd """
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * formoas.dasd")
    a = []
    for row in cur.fetchall():
        print(row)
        a.append(row)
    db.close()
    return a

def q_global_month():
    """ asd """
    db = MySQLdb.connect(host=SQL_ADDRESS,    # your host, usually localhost
                         user=SQL_USER,         # your username
                         passwd=SQL_PASS,  # your password
                         db=SQL_DB)        # name of the data base
    cur = db.cursor()
    cur.execute("SLEC")
    a = []
    for row in cur.fetchall():
        print(row)
        a.append(row)
    db.close()
    return a
