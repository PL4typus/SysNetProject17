#!/usr/bin/python

from M2Crypto import RSA, EVP
import base64, hashlib
 
pkey = RSA.load_key("mykey.pem") 
signText = pkey.sign(hashlib.sha256("Text_test.txt").digest())
print ("fin")

