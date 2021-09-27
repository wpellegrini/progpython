#!/usr/bin/python

import whois
msg_domain = "Informe o nome do dominio alvo" 
target="google.com"
#querywhois = whois.query(target)

querywhois = whois.query(target)


def func_whois():
    print("[+] - Nome do dominio: ", querywhois.name)
    print("[+] - Data de criacao: ", querywhois.creation_date)
    print("[+] - Data de expiracao: ", querywhois.expiration_date)
    print("[+] - Data de ultimo atualizacao: ",querywhois.last_updated)
    print("[+] - Servidor Whois registrado:", querywhois.registrar)

    for _domain in querywhois.name_servers:
        print("[+] - Servidor de nomes: ", _domain)



func_whois
