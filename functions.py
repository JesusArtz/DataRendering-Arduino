from conn import get_db

def insert_temp(valor):
    db = get_db()
    cursor = db.cursor()
    query = f"INSERT INTO temperatura VALUES (NULL, {valor})"
    print(query)
    cursor.execute(query)
    db.commit()
    return True


def insert_humedad(valor):
    db = get_db()
    cursor = db.cursor()
    query = f"INSERT INTO humedad VALUES (NULL, {valor})"
    print(query)
    cursor.execute(query)
    db.commit()
    return True



def get_humedad():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, humedad FROM humedad ORDER BY id DESC LIMIT 50"
    cursor.execute(query)
    return cursor.fetchall()    

def get_temp():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, temperatura FROM temperatura ORDER BY id DESC LIMIT 50"
    cursor.execute(query)
    return cursor.fetchall()