#coding:utf8

import argparse
import dns.resolver

def DNSAttack(name):
    t = 0
    while True:
        t = t+1
        for qtype in  'A', 'AAAA', 'CNAME', 'MX', 'NS':
            try:
                answer = dns.resolver.query(name,qtype,raise_on_no_answer=False)
            except dns.resolver.NXDOMAIN:
                print("Shit it!Are you sure the domain is correct?")
                exit()
            if answer.rrset is not None:
                print("Results:\n")
                print(answer.rrset)
                #print("\n\n")
                print("Atttacked %s times." % str(t))
            #else:
                #print("The name of %s is not found." % qtype)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS")
    parser.add_argument("name",help="The domain that you want to Attack.\
(You need to input the root domain)")
    DNSAttack(parser.parse_args().name)

