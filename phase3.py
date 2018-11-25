from bsddb3 import db
database = db.DB()
database.open('ad.idx',None, db.DB_HASH)