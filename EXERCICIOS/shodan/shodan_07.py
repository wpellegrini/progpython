#!/usr/bin/python

import time
import shodan
shodan_mykey='kdnzf4fsYWQmGajRDn3hB0RElbUlIaqu'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)

def shodan_info():
    print ('[*] - Informações genericas do ALVO')
    print('IP alvo:',shodan_host['ip_str'])
    print('Organizacao:', shodan_host.get('org','n/a'))
    print('Sistema Operacional:', shodan_host.get('os','n/a'))
    print('-' * 60)

def shodan_portscan():
    print('[*] - Identificação de portas abertas')
    
    for _line in shodan_host['data']:
            print("[+] - Porta Aberta:", _line['port']) 
            print("[+] - Banner:", _line['data'])
            print("-" * 60)        

def shodan_vuln():
    print('[*] - Lista de possiveis Vulnerabilidade:')
            
    for item in shodan_host['vulns']:
        time.sleep(0.5)
        CVE = item.replace('!' , '')
        print('[+] Vunerability', item)
        
        exploits = shodan_api.exploits.search(CVE)
        
        for item in exploits['matches']:
            try:
                if item.get('cve')[0] == CVE:
                    print('[++]) - Vulnerabilidade / CVE')
                    print(item.get('description'))
                    print()

            except:
               print('[!] - Descrição não disponivel')



print("-" * 60)
print("-" * 60)
shodan_info()
print("-" * 60)
shodan_portscan()
print("_" * 60)
shodan_vuln()
print("-" * 60)
