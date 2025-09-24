from mysql.connector import (connection)
from db_operation import operation

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='shopping')
if not cnx.is_connected():
    print("Errore di connessione al database.")
    exit()

cursor = cnx.cursor()



max_products = 10

id = operation.login(cursor)
if not id:
    print("Impossibile accedere. Uscita dal programma.")
    cnx.close()
    exit()

while True:
    print("")
    print("--------------------------------") 
    print("Menu:")
    print("1. Aggiungi prodotto")
    print("2. Rimuovi prodotto")
    print("3. Visualizza lista")
    print("4. Svuota lista")
    print("5. Elimina utente")
    print("6. Cambia utente")
    print("7. Esci")
    print("")
    
    choise = input("Scegli un'opzione (1-6): ")
    print("\n")
    if choise == '1':
        operation.add(id, cursor, max_products)
        cnx.commit()
    elif choise == '2':
        operation.remove(id, cursor)
        cnx.commit()
    elif choise == '3':
        operation.list(id, cursor)
    elif choise == '4':
        operation.empty(id, cursor)
        cnx.commit()
    elif choise == '5':
        operation.delete_id(id, cursor)
        print("Utente eliminato. Uscita dal programma.")
        cnx.commit()
        cnx.close()
        break
    elif choise == '6':
        new_id = operation.login(cursor)
        if not new_id:
            print("Impossibile accedere. Uscita dal programma.")
            cnx.commit()
            cnx.close()
            break
        id = new_id
    elif choise == '7':
        print("Uscita dal programma.")
        cnx.close()
        break
    else:
        print("Opzione non valida. Riprova.")