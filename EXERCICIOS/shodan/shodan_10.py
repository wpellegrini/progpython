#!/usr/bin/python

import shodan
shodan_mykey='kdnzf4fsYWQmGajRDn3hB0RElbUlIaqu'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_item='Microsoft-IIS/8.0 country'
shodan_result = shodan_api.search(shodan_item)


def shodan_search():
    print('buscar por:', shodan_item)
    print('Numero de ocorrencias:', shodan_result['total'])
    
    print('.....TOP 100.....')

    count = 1 
    
    for _result in shodan_result['matches']:  
        print('[+] - Possivel alvo',count, 'IP:', _result['ip_str'])
        count = count +1


shodan_search()
