#  CNA 350 Realworld Project
#  Instructor: Zach Rubin, zrubin@rtc.edu
#  Christiana Freeman, csfreeman@student.rtc.edu
#  with help from TJ Dewey, tjdewey@student.rtc.edu
#  sources: stackoverflow.com


import mysql.connector

def connect():
     server_ip = ## add your server's IP here IN QUOTATION ##
     conn = mysql.connector.connect(host=server_ip, user='maxuser', password='maxpwd', port='4000')
     return conn


def question_one(cursor):
    query = SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 10
     cursor.execute(query)
     answer = cursor.fetchall()
     print ('Last 10 of zipcodes 1')
     for row in answer:
          print (row)
     return

def question_two(cursor):
     query = SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 10
     cursor.execute(query)
     answer = cursor.fetchall()
     print ('First 10 of zipcodes 2')
     for row in answer:
          print (row)
     return

def question_three(cursor):
     query = ## first SQL query here, in quotation ##
     cursor.execute(query)
     answer = cursor.fetchall()
     print ('Largest in zipcodes 1')
     for row in answer:
          print (row)
     return

def question_four(cursor):
     query = ## first SQL query here, in quotation ##
     cursor.execute(query)
     answer = cursor.fetchall()
     print ('smallest in zipcodes 2')
     for row in answer:
          print (row)
     return

def main():
     conn = connect()
     curs = conn.cursor()

     question_one(curs)
     question_two(curs)
     question_three(curs)
     question_four(curs)

     conn.close()
     
if __name__ == '__main__':
     main()
