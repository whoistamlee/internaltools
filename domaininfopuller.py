from re import M
import whois
import sys

#can use to figure out expiration date
while True:
    try:
        while True:
            print(whois.whois(input("Input: ")))
    except:
        sys.exit