import mysql.connector
from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class CorsoDao:

    @staticmethod
    def get_all_corsi():

        cnx = DBConnect.get_connection()

        result = []

        if cnx is None:
            print("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                    FROM corso c """
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

            cursor.close()
            cnx.close()

            return result


    @staticmethod  #per eseguire il metodo anche senza avere una instanza della classe
    def get_corsi_periodo(pd):

        cnx = DBConnect.get_connection()

        result = []

        if cnx is None:
            print("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                    FROM corso c
                    WHERE c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

            cursor.close()
            cnx.close()

            return result

    @staticmethod
    def get_studenti_periodo(pd):

        cnx = DBConnect.get_connection()

        result = 0

        if cnx is None:
            print("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT COUNT(DISTINCT i.matricola)
                    FROM corso c, iscrizione i
                    WHERE c.pd = %s AND i.codins = c.codins"""

            cursor.execute(query, (pd,))

            if cursor.with_rows:
                result = cursor.fetchone()[0]


            cursor.close()
            cnx.close()

            return result

    @staticmethod
    def get_matricole_corso(codins):
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Errore di connessione")
            return None
        else:
            result = set()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT i.matricola
                        FROM iscrizione i
                        WHERE i.codins = %s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                result.add(row["matricola"])

            cursor.close()
            cnx.close()

            return result

    @staticmethod
    def get_studenti_corso(codins):
        cnx = DBConnect.get_connection()

        result = []

        if cnx is None:
            print("Errore di connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.*
                    FROM iscrizione i, studente s 
                    WHERE i.matricola = s.matricola AND i.codins = %s"""

            cursor.execute(query, (codins,))

            for row in cursor:
                result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))

            #print(result)
            cursor.close()
            cnx.close()

            return result

