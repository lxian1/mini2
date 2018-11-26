from bsddb3 import db


def usr_interface():
    while True:
        print('1.camera\n2.camera%\n3.date <= 2018/11/05\n4.date > 2018/11/05\n5.price < 20\n6.price >= 20\n7.location=edmonton date=2018/11/07\n8.cat=art-collectibles camera\n9.camera date>=2018/11/05 date<=2018/11/07 price > 20 price < 40\n10.switch output\n11.exit')
        query = input('Please enter 1-11 to select a query or command: ')
        if query == '1':
            pass
        if query == '2':
            pass
        if query == '3':
            pass
        if query == '4':
            pass
        if query == '5':
            pass
        if query == '6':
            pass
        if query == '7':
            pass
        if query == '8':
            pass
        if query == '9':
            pass
        if query == '10':
            pass
        if query == '11':
            print('The program is closing...')
            print('Adiós')
            return False

def main():
    #usr_interface()
    
    #access to the idxed database
    database = db.DB()
    DB_File = "pr.idx"
    database.open(DB_File, None, db.DB_BTREE, db.DB_RDONLY)
    
main()