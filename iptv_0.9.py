#!/usr/bin/python
import Crawler
import warnings
from clint.textui import colored


warnings.filterwarnings("ignore")
cr = Crawler.Crawler("it")

def menu():
    print ""
    print colored.black("################################")
    print colored.black("#####      ####        #########")
    print colored.red("#####      #######  ############")
    print colored.red("#####  ###########  ############")
    print colored.yellow("#####  ## ######    ## #########")
    print colored.yellow("################################")
    print ""
    print "IPTV v0.9 by pjor94"
    print ""
    print colored.blue("Menu IPtv")
    print "0 - Esci"
    print "1 - Cerca per server su google "
    print "2 - Vedi lista Server"
    print "3 - Brute force su un server a random"
    print "4 - Brute force su un server specifico"
    print ""

while True:
    menu()
    SceltaMenu = int(raw_input("Selezionare un opzione: "))
    if SceltaMenu == 0:
        print colored.red("Addio")
        break;
    elif SceltaMenu == 1:
        print colored.green("Cercando Server, attendi")
        cr.search_links()
        print colored.green("Fatto, 15 URLs trovati")
    elif SceltaMenu == 2:
        print colored.green("Stampo lista dei server")
        for index, server in enumerate(cr.parsedUrls):
            print "[" + str(index) + "] - " + server
    elif SceltaMenu == 3:
        result =  cr.search_accounts()
        print colored.green(result)
    elif SceltaMenu == 4:
        index = int(raw_input("Inserisci il numero difianco al URL del server: "))
        try:
            url = cr.parsedUrls[index]
            result = cr.search_accounts(url)
            print colored.green(result)
        except IndexError as e:
            print colored.red("Nessun URL trovato per: " + str(index)) 
    else:
        print colored.red("Opzione non riconosciuta")
