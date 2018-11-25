from bsddb3 import db

def main():
    database = db.DB()
    DB_File = "project2.db"
    database.open(DB_File ,None, db.DB_HASH, db.DB_CREATE)
    curs = database.cursor()
    for i in pairs:
        database.put(b(i))
               
main() 