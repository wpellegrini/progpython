#!/usr/bin/python

import dns.query
import dns.zone



domain = 'yellow.dojo'
target = 'ns.yellow.dojo' 

try:
  transfzone = dns.zone.from_xfr(dns.query.xfr(target, domain))
 
  for _machines in transfzone:
      print('[+] -', str(_machines) + "." + domain)

except:
    print('[!] - Falha na transferência de zona de dominio:', domain, 'NS:', target)












