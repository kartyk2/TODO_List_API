import pymysql.cursors


# Connect to the database
def connect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kartyk',
                                 database='TODO',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


cnx = connect()
