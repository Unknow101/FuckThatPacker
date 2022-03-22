#!/usr/bin/python3
import base64
import argparse
import re
import os

def xor_payload(payload,key):
        return ''.join(chr(ord(a) ^ key) for a in payload)


banner = '''
  ___        _   _____ _         _   ___         _           
 | __|  _ __| |_|_   _| |_  __ _| |_| _ \__ _ __| |_____ _ _ 
 | _| || / _| / / | | | ' \/ _` |  _|  _/ _` / _| / / -_) '_|
 |_| \_,_\__|_\_\ |_| |_||_\__,_|\__|_| \__,_\__|_\_\___|_|  
                                                          
                                                                      '''
version = "v1.0"
print (banner)
print ("Written with <3 by Unknow101/inf0sec")
print (version+"\n\n")
parser = argparse.ArgumentParser()
parser.add_argument("-k","--key", help="integer key use of XOR operation",type=int,dest='key',required=True)
parser.add_argument("-p","--payload",help="path of the payload to pack",type=str,dest='payload',required=True)
parser.add_argument("-o","--output",help="output payload into file",type=str,dest="output")
args = parser.parse_args()
key = args.key

with open(args.payload) as f:
        content = f.read()

print "[+] Encode UTF16-LE"
content = content.encode("utf-16-le")
print "[+] Cyphering Payload ..."
content = xor_payload(content,key)

print "[+] Base64 Payload"
content = base64.b64encode(content)

print "[+] Writting into Template"
path = os.path.dirname(os.path.abspath(__file__))
with open(path+"/template.txt") as f:
        template = f.read()

template = template.replace("%%DATA%%",content)
template = template.replace("%%KEY%%",str(key))

if args.output:
        print ("[+] Writting into " + args.output)
        with open(args.output,"w") as f:
                f.write(template)
else:
        print (template)
