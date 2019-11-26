import mysql.connector




def IsFaculty_IDTaken(faculty_id):
    cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
    cursor = cnx.cursor()

    query = ("SELECT COUNT(*) FROM faculty f WHERE f.faculty_id = %s")

    cursor.execute(query, (faculty_id,))
    result = cursor.fetchone()[0]
    cnx.close()
    if result > 0:
      return True
    else:
      return False

def CheckLoginCredentials(username, password):
    cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
    cursor = cnx.cursor()

    query = ("SELECT COUNT(*) FROM faculty f WHERE f.username = %s AND f.password = %s;")

    cursor.execute(query, (username, password))
    result = cursor.fetchone()[0]
    cnx.close()
    if result > 0:
      return True
    else:
      return False
