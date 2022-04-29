import sys, re
import requests

f = open('log.txt','r')
text = f.read()
ips = [] 
x = []
re_ip = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",text)
re_port = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:(\d+)",text)

if re_ip is not None:
    for match in re_ip:
        if match not in ips:
            x = ips.append(match)
            print(match)


if re_ip is not None:
    for match in re_port:
        if match not in ips:
            x = ips.append(match)
            print(match)
