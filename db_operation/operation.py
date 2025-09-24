def list(number,cursor):
    cursor.execute("SELECT oggetto FROM spesa WHERE id_utente = %s",(number,))
    spesa = cursor.fetchall()
    if not spesa:
        print("la lista è vuota")
        return
    for e in range(len(spesa)):
        spesa[e] = spesa[e][0]
        print(f"{e+1}. {spesa[e]}")


def add(id,cursor,max):
    cursor.execute("SELECT COUNT(*) FROM spesa WHERE id_utente = %s",(id,))
    num = cursor.fetchone()[0]
    if num >= max:
        print("hai raggiunto il numero massimo di prodotti")
        return
    product = input("inserisci il prodotto da aggiungere: ")
    product = product.strip()
    product = product.lower()
    if not product:
        print("input non valido")
        return
    cursor.execute("SELECT oggetto FROM spesa WHERE id_utente = %s AND oggetto = %s",(id,product))
    exist = cursor.fetchone()
    if exist:
        print("il prodotto è già presente nella lista")
        return
    cursor.execute("INSERT INTO spesa (id_utente, oggetto) VALUES (%s, %s)",(id,product))
    print(f"{product} aggiunto alla lista della spesa.")
    
    
def remove(id,cursor):
    cursor.execute("SELECT oggetto FROM spesa WHERE id_utente = %s",(id,))
    shop = cursor.fetchall()
    if not shop:
        print("la lista è vuota")
        return
    for e in range(len(shop)):
        shop[e] = shop[e][0]
        print(f"{e+1}. {shop[e]}")
    choise = input("inserisci il numero del prodotto da rimuovere: ")
    if not choise.isdigit():
        print("input non valido")
        return
    choise = int(choise)
    if choise < 1 or choise > len(shop):
        print("input non valido")
        return
    product = shop[choise-1]
    cursor.execute("DELETE FROM spesa WHERE id_utente = %s AND oggetto = %s",(id,product))
    print(f"{product} rimosso dalla lista della spesa.")
    
    
def empty(id,cursor):
    cursor.execute("SELECT oggetto FROM spesa WHERE id_utente = %s",(id,))
    shop = cursor.fetchall()
    if not shop:
        print("la lista è già vuota")
        return
    confirm = input("sei sicuro di voler svuotare la lista? (s/n): ")
    if confirm.lower() != 's':
        print("operazione annullata")
        return
    cursor.execute("DELETE FROM spesa WHERE id_utente = %s",(id,))

    print("lista della spesa svuotata.")
    

def login(cursor):
    name = input("inserisci il tuo nome: ")
    name = name.strip()
    name = name.lower()
    print("")
    cursor.execute("SELECT id FROM utenti WHERE nome = %s",(name,))
    id = cursor.fetchone()
    if id:
        print(f"bentornato/a {name}")
        return id[0]
    else:
        cursor.execute("insert INTO utenti (nome) VALUES (%s)",(name,))
        cursor.execute("SELECT id FROM utenti WHERE nome = %s",(name,))
        id = cursor.fetchone()
        if id:
            print("Utente registrato con successo.")
            return id[0]
        else:
            print("Errore nella registrazione dell'utente.")
            return None


    
def delete_id(id,cursore):
    conferma = input("sei sicuro di voler eliminare il tuo utente e tutti i prodotti associati? (s/n): ")
    if conferma.lower() != 's':
        print("operazione annullata")
        return
    cursore.execute("DELETE FROM spesa WHERE id_utente = %s",(id,))
    cursore.execute("DELETE FROM utenti WHERE id = %s",(id,))
    print("utente e lista della spesa eliminati.")