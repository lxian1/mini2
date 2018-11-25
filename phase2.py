from bsddb3 import db

def main():
    pairs = []
    with open('ads.txt','r') as file:
        d = file.readlines()
        for line in d:
            pairs.append(line.split(':'))
        file.close()
    database = db.DB()
    DB_File = "project2.db"
    database.open(DB_File ,None, db.DB_HASH, db.DB_CREATE)
    curs = database.cursor()
    for i in pairs:
        database.put(b(i))
               
main() 