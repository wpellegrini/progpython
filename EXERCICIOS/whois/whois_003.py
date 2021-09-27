#! /usr/bin/python

import whois

target = "google.com"

def func_whois(_domain):
    querywhois = whois.query(_domain)
    print("[+] - Nome do dominio: ", querywhois.name)
    print("[+] - Data de criacao: ", querywhois.creation_date)
    print("[+] - Data de expiracao: ", querywhois.expiration_date)
    print("[+] - Data de ultimo atualizacao:", querywhois.last_updated)
    print("[+] - Servidor Whois registrado:", querywhois.registrar)

    for _domain in querywhois.name_servers:
        print(_domain)

func_whois(target)
