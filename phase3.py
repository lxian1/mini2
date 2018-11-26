from bsddb3 import *
import bsddb3
import sys

def usr_interface():
    while True:
        print('1.camera\n2.camera%\n3.date <= 2018/11/05\n4.date > 2018/11/05\n5.price < 20\n6.price >= 20\n7.location=edmonton date=2018/11/07\n8.cat=art-collectibles camera\n9.camera date>=2018/11/05 date<=2018/11/07 price > 20 price < 40\n10.exit')
        query = input('Please enter 1-10 to select a query: ')
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
            print('The program is closing...')
            print('Adiós!')
            return False

def main():
    #TODO: Access to idx database 
    #database = db.DB()
    #DB_File = "ad.idx"
    #bsddb3.hashopen(DB_File,'c')
    usr_interface()
    
main()